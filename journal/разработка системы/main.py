"""
main.py — точка входа SEO Site Health Monitor.

Алгоритм:
  1. Загрузить clients.csv
  2. Для каждого клиента: scan_site() → calculate_seo_score() → assign_priority()
  3. Сохранить в SQLite
  4. Сравнить с audit_history.csv (если есть данные по клиенту)
  5. Вывести console report + алерты
  6. Сохранить CSV report
"""
import csv
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from rich.console import Console

sys.path.insert(0, str(Path(__file__).parent))

from src.scanner import scan_site
from src.analyzer import calculate_seo_score, assign_priority
from src.database import init_db, save_audit, get_last_audit
from src.reporter import generate_console_report, generate_csv_report, generate_delta_report
from src.notifier import check_alerts, print_alerts

console = Console()


def _setup_logging(log_file: str) -> None:
    Path(log_file).parent.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s %(name)s — %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def _load_config() -> dict:
    with open("config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _load_clients(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _load_audit_history(path: str) -> dict[str, dict]:
    history: dict[str, dict] = {}
    try:
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                cid = row.get("client_id")
                history[cid] = row
    except FileNotFoundError:
        pass
    return history


def main() -> None:
    cfg = _load_config()
    files = cfg.get("files", {})

    _setup_logging(files.get("log_file", "logs/audit.log"))
    logger = logging.getLogger(__name__)

    console.print("[bold cyan]🔍 SEO Site Health Monitor — DELTA Web Studio[/bold cyan]")
    console.print(f"Запуск: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    init_db()

    clients = _load_clients(files.get("clients_csv", "data/clients.csv"))
    history_map = _load_audit_history(files.get("audit_history_csv", "data/audit_history.csv"))

    audits_current = []
    audits_previous_for_delta = []

    for client in clients:
        cid = client["client_id"]
        name = client.get("client_name", cid)
        url = client["site_url"]

        console.print(f"[yellow]→ Сканирую:[/yellow] {name} ({url})")

        scan = scan_site(url)
        score = calculate_seo_score(scan)
        prev_db = get_last_audit(cid)
        prev_audit = prev_db if prev_db else history_map.get(cid)

        client_with_broken = {**client, "broken_links_count": scan.get("broken_links_count", 0)}
        priority = assign_priority(client_with_broken, prev_audit, score)

        record = {
            "client_id":          cid,
            "url":                url,
            "scan_date":          scan.get("scan_timestamp", datetime.now(timezone.utc).isoformat()),
            "status_code":        scan.get("status_code"),
            "title":              scan.get("title"),
            "title_length":       scan.get("title_length", 0),
            "has_description":    scan.get("has_description", False),
            "description_length": scan.get("description_length", 0),
            "has_h1":             scan.get("has_h1", False),
            "h1_text":            scan.get("h1_text"),
            "ttfb_ms":            scan.get("ttfb_ms"),
            "html_size_kb":       scan.get("html_size_kb", 0.0),
            "has_ssl":            scan.get("has_ssl", False),
            "broken_links_count": scan.get("broken_links_count", 0),
            "seo_score":          score,
            "priority":           priority,
        }

        save_audit(record)

        alerts = check_alerts(record, prev_audit)
        print_alerts(cid, name, alerts)

        audits_current.append(record)
        if prev_audit:
            audits_previous_for_delta.append({**prev_audit, "client_id": cid})

    console.print("\n")
    generate_console_report(audits_current)

    if audits_previous_for_delta:
        generate_delta_report(audits_current, audits_previous_for_delta)

    Path("reports").mkdir(exist_ok=True)
    report_path = files.get("report_csv", "reports/audit_report.csv")
    generate_csv_report(audits_current, report_path)

    console.print("\n[bold green]✅ Аудит завершён![/bold green]")
    logger.info("Audit completed. %d sites scanned.", len(clients))


if __name__ == "__main__":
    main()
