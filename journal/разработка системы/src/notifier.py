"""
notifier.py — консольные алерты для критических проблем.
"""
import yaml
import logging
from rich.console import Console

logger = logging.getLogger(__name__)
console = Console()


def _load_config() -> dict:
    with open("config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_alerts(audit: dict, previous_audit: dict | None = None) -> list[str]:
    cfg = _load_config()
    t = cfg.get("thresholds", {})
    ttfb_warn = t.get("ttfb_warning_ms", 3000)
    broken_crit = t.get("broken_links_critical", 3)
    score_drop_threshold = t.get("score_drop_alert", 10)

    alerts = []

    if previous_audit and previous_audit.get("seo_score") is not None:
        prev_score = int(previous_audit["seo_score"])
        cur_score = audit.get("seo_score")
        if cur_score is not None:
            drop = prev_score - cur_score
            if drop > score_drop_threshold:
                alerts.append(f"[ALERT] SEO-score упал на {drop} пунктов ({prev_score} → {cur_score})")

    broken = audit.get("broken_links_count", 0)
    if broken >= broken_crit:
        alerts.append(f"[ALERT] Обнаружено {broken} битых ссылок")

    ttfb = audit.get("ttfb_ms")
    if ttfb is not None and ttfb > ttfb_warn:
        alerts.append(f"[ALERT] TTFB {ttfb:.0f} мс (порог {ttfb_warn} мс)")

    if audit.get("status_code") not in (200, None) and audit.get("status_code", 0) != 200:
        alerts.append(f"[ALERT] Сайт вернул HTTP {audit.get('status_code')}")

    if not audit.get("has_ssl"):
        alerts.append("[ALERT] Сайт работает без SSL (HTTP)")

    return alerts


def print_alerts(client_id: str, client_name: str, alerts: list[str]) -> None:
    if not alerts:
        return
    console.print(f"\n[bold red]🚨 Алерты для {client_name} ({client_id}):[/bold red]")
    for alert in alerts:
        console.print(f"  [red]{alert}[/red]")
    logger.warning("Alerts for %s: %s", client_id, alerts)
