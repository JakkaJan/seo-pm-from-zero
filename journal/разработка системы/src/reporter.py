"""
reporter.py — генерация консольного и CSV отчётов, delta-сравнение.
"""
import csv
import logging
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich import box

logger = logging.getLogger(__name__)
console = Console()

PRIORITY_COLORS = {
    "P0": "bold red",
    "P1": "bold yellow",
    "P2": "green",
    "P3": "dim",
}

SCORE_COLORS = {
    "critical": "bold red",
    "warning":  "yellow",
    "ok":       "green",
}


def _score_color(score: int | None) -> str:
    if score is None:
        return "dim"
    if score < 50:
        return SCORE_COLORS["critical"]
    if score < 70:
        return SCORE_COLORS["warning"]
    return SCORE_COLORS["ok"]


def generate_console_report(audits: list) -> None:
    table = Table(
        title="[bold cyan]SEO Site Health Monitor — DELTA[/bold cyan]",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        show_lines=True,
    )

    table.add_column("Client ID",  style="cyan",   width=8)
    table.add_column("URL",        style="white",  width=30, overflow="fold")
    table.add_column("Status",     justify="center", width=7)
    table.add_column("Score",      justify="center", width=7)
    table.add_column("Priority",   justify="center", width=8)
    table.add_column("TTFB (ms)",  justify="right",  width=10)
    table.add_column("SSL",        justify="center", width=5)
    table.add_column("H1",         justify="center", width=5)
    table.add_column("Broken",     justify="center", width=7)
    table.add_column("Title len",  justify="center", width=9)
    table.add_column("Scan date",  width=22)

    for a in audits:
        score = a.get("seo_score")
        priority = a.get("priority", "P3")
        status = a.get("status_code", "?")
        ttfb = a.get("ttfb_ms")

        status_str = f"[green]{status}[/green]" if status == 200 else f"[red]{status}[/red]"
        score_str = f"[{_score_color(score)}]{score}[/{_score_color(score)}]" if score is not None else "—"
        prio_str = f"[{PRIORITY_COLORS.get(priority, 'white')}]{priority}[/{PRIORITY_COLORS.get(priority, 'white')}]"
        ttfb_str = f"{ttfb:.0f}" if ttfb else "—"
        ssl_str = "[green]✓[/green]" if a.get("has_ssl") else "[red]✗[/red]"
        h1_str = "[green]✓[/green]" if a.get("has_h1") else "[red]✗[/red]"
        broken = a.get("broken_links_count", 0)
        broken_str = f"[red]{broken}[/red]" if broken >= 3 else f"[yellow]{broken}[/yellow]" if broken > 0 else "[green]0[/green]"
        tlen = a.get("title_length", 0)
        tlen_str = f"[green]{tlen}[/green]" if 30 <= tlen <= 60 else f"[yellow]{tlen}[/yellow]"
        scan_date = a.get("scan_date", "")[:19]

        table.add_row(
            a.get("client_id", ""),
            a.get("url", a.get("site_url", "")),
            status_str, score_str, prio_str, ttfb_str,
            ssl_str, h1_str, broken_str, tlen_str, scan_date,
        )

    console.print(table)


def generate_csv_report(audits: list, filename: str) -> None:
    fieldnames = [
        "client_id", "url", "scan_date", "status_code",
        "title", "title_length", "has_description", "description_length",
        "has_h1", "h1_text", "ttfb_ms", "html_size_kb",
        "has_ssl", "broken_links_count", "seo_score", "priority",
    ]
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for a in audits:
            row = {k: a.get(k, "") for k in fieldnames}
            writer.writerow(row)
    logger.info("CSV report saved: %s (%d rows)", filename, len(audits))
    console.print(f"[green]✓ CSV отчёт сохранён:[/green] {filename}")


def generate_delta_report(current: list, previous: list) -> None:
    prev_map = {p.get("client_id"): p for p in previous}
    console.print("\n[bold cyan]📊 Delta-отчёт: сравнение с предыдущим аудитом[/bold cyan]")
    table = Table(box=box.SIMPLE, header_style="bold blue", show_lines=False)
    table.add_column("Client ID", width=8)
    table.add_column("Пред. score", justify="center", width=12)
    table.add_column("Тек. score",  justify="center", width=12)
    table.add_column("Δ score",     justify="center", width=10)
    table.add_column("Пред. broken", justify="center", width=14)
    table.add_column("Тек. broken",  justify="center", width=13)

    for c in current:
        cid = c.get("client_id")
        prev = prev_map.get(cid)
        cur_score = c.get("seo_score")
        prev_score = int(prev["seo_score"]) if prev and prev.get("seo_score") is not None else None
        if prev_score is not None and cur_score is not None:
            delta = cur_score - prev_score
            delta_str = f"[green]+{delta}[/green]" if delta >= 0 else f"[red]{delta}[/red]"
        else:
            delta_str = "—"
        prev_broken = str(prev.get("broken_links", "—")) if prev else "—"
        cur_broken = str(c.get("broken_links_count", "—"))
        table.add_row(
            cid or "",
            str(prev_score) if prev_score is not None else "нет данных",
            str(cur_score) if cur_score is not None else "—",
            delta_str, prev_broken, cur_broken,
        )
    console.print(table)
