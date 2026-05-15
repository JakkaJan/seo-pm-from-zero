"""
analyzer.py — расчёт SEO-score (0–100) и расстановка приоритетов P0–P3.
"""
import yaml
from datetime import datetime, timezone


def _load_config() -> dict:
    with open("config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def calculate_seo_score(scan_result: dict) -> int:
    """
    Рассчитывает SEO-score по формуле из ТЗ.

    Баллы:
        status_code 200         → 20
        title 30–60 символов    → 15
        has_description + 120–160 → 15
        has_h1                  → 10
        ttfb < 1000 мс          → 20  |  < 3000 мс → 10
        has_ssl                 → 10
        broken_links == 0       → 10  |  <= 2 → 5
    Итого: 100
    """
    cfg = _load_config()
    t = cfg.get("thresholds", {})
    title_min = t.get("title_optimal_min", 30)
    title_max = t.get("title_optimal_max", 60)
    desc_min  = t.get("description_optimal_min", 120)
    desc_max  = t.get("description_optimal_max", 160)

    score = 0

    if scan_result.get("status_code") == 200:
        score += 20

    tlen = scan_result.get("title_length", 0)
    if title_min <= tlen <= title_max:
        score += 15

    if scan_result.get("has_description"):
        dlen = scan_result.get("description_length", 0)
        if desc_min <= dlen <= desc_max:
            score += 15

    if scan_result.get("has_h1"):
        score += 10

    ttfb = scan_result.get("ttfb_ms")
    if ttfb is not None:
        if ttfb < 1000:
            score += 20
        elif ttfb < 3000:
            score += 10

    if scan_result.get("has_ssl"):
        score += 10

    broken = scan_result.get("broken_links_count", 0)
    if broken == 0:
        score += 10
    elif broken <= 2:
        score += 5

    return min(score, 100)


def assign_priority(client_data: dict, previous_audit: dict | None, current_score: int) -> str:
    """
    Расставляет приоритет P0–P3.

    P0: Премиум + (score < 50 ИЛИ broken_links >= 3 ИЛИ score упал > 10 за месяц)
    P1: Стандарт + (score < 60 ИЛИ запуск < 6 месяцев назад)
    P2: Базовый + score >= 60
    P3: Всё остальное
    """
    package = client_data.get("seo_package", "")
    launch_date_str = client_data.get("launch_date", "")
    broken = client_data.get("broken_links_count", 0)

    score_drop = 0
    if previous_audit and previous_audit.get("seo_score") is not None:
        score_drop = int(previous_audit["seo_score"]) - current_score

    site_age_months = None
    if launch_date_str:
        try:
            launch = datetime.fromisoformat(launch_date_str)
            now = datetime.now(timezone.utc).replace(tzinfo=None)
            delta = now - launch
            site_age_months = delta.days / 30
        except ValueError:
            pass

    if package == "Премиум":
        if current_score < 50 or broken >= 3 or score_drop > 10:
            return "P0"

    if package == "Стандарт":
        if current_score < 60 or (site_age_months is not None and site_age_months < 6):
            return "P1"

    if package == "Базовый" and current_score >= 60:
        return "P2"

    return "P3"
