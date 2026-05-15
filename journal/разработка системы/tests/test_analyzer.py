"""
test_analyzer.py — тесты расчёта seo_score и assign_priority.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.analyzer import calculate_seo_score, assign_priority


def _perfect_scan():
    return {
        "status_code": 200,
        "title_length": 45,
        "has_description": True,
        "description_length": 140,
        "has_h1": True,
        "ttfb_ms": 500,
        "has_ssl": True,
        "broken_links_count": 0,
    }


def test_perfect_score_is_100():
    assert calculate_seo_score(_perfect_scan()) == 100

def test_missing_ssl_loses_10():
    assert calculate_seo_score({**_perfect_scan(), "has_ssl": False}) == 90

def test_broken_links_2_loses_5():
    assert calculate_seo_score({**_perfect_scan(), "broken_links_count": 2}) == 95

def test_broken_links_3_loses_10():
    assert calculate_seo_score({**_perfect_scan(), "broken_links_count": 3}) == 90

def test_slow_ttfb_under_3000_gives_10():
    assert calculate_seo_score({**_perfect_scan(), "ttfb_ms": 2000}) == 90

def test_very_slow_ttfb_gives_0():
    assert calculate_seo_score({**_perfect_scan(), "ttfb_ms": 4000}) == 80

def test_bad_title_length_loses_15():
    assert calculate_seo_score({**_perfect_scan(), "title_length": 10}) == 85

def test_no_description_loses_15():
    assert calculate_seo_score({**_perfect_scan(), "has_description": False, "description_length": 0}) == 85

def test_status_not_200_loses_20():
    assert calculate_seo_score({**_perfect_scan(), "status_code": 500}) == 80

def test_zero_scan_returns_0():
    assert calculate_seo_score({
        "status_code": 500, "title_length": 5, "has_description": False,
        "description_length": 0, "has_h1": False, "ttfb_ms": 9000,
        "has_ssl": False, "broken_links_count": 10,
    }) == 0

def test_premium_low_score_is_p0():
    client = {"seo_package": "Премиум", "launch_date": "2023-01-01", "broken_links_count": 0}
    assert assign_priority(client, None, 45) == "P0"

def test_premium_broken_links_is_p0():
    client = {"seo_package": "Премиум", "launch_date": "2023-01-01", "broken_links_count": 5}
    assert assign_priority(client, None, 80) == "P0"

def test_premium_score_drop_is_p0():
    client = {"seo_package": "Премиум", "launch_date": "2023-01-01", "broken_links_count": 0}
    assert assign_priority(client, {"seo_score": 80}, 65) == "P0"

def test_standard_low_score_is_p1():
    client = {"seo_package": "Стандарт", "launch_date": "2022-01-01", "broken_links_count": 0}
    assert assign_priority(client, None, 55) == "P1"

def test_standard_new_site_is_p1():
    from datetime import datetime, timedelta
    recent = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    client = {"seo_package": "Стандарт", "launch_date": recent, "broken_links_count": 0}
    assert assign_priority(client, None, 75) == "P1"

def test_basic_good_score_is_p2():
    client = {"seo_package": "Базовый", "launch_date": "2022-01-01", "broken_links_count": 0}
    assert assign_priority(client, None, 70) == "P2"

def test_unknown_package_is_p3():
    client = {"seo_package": "Неизвестный", "launch_date": "2022-01-01", "broken_links_count": 0}
    assert assign_priority(client, None, 80) == "P3"
