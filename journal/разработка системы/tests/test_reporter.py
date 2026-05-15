"""
test_reporter.py — тесты генерации CSV-отчёта.
"""
import csv
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.reporter import generate_csv_report

SAMPLE_AUDITS = [
    {
        "client_id": "C001", "url": "https://example.com",
        "scan_date": "2026-05-16T10:00:00+00:00", "status_code": 200,
        "title": "Тест", "title_length": 4, "has_description": True,
        "description_length": 130, "has_h1": True, "h1_text": "Заголовок",
        "ttfb_ms": 450.0, "html_size_kb": 32.1, "has_ssl": True,
        "broken_links_count": 0, "seo_score": 85, "priority": "P2",
    },
    {
        "client_id": "C002", "url": "https://slow-site.ru",
        "scan_date": "2026-05-16T10:05:00+00:00", "status_code": 200,
        "title": "Медленный сайт без описания", "title_length": 27,
        "has_description": False, "description_length": 0, "has_h1": False,
        "h1_text": None, "ttfb_ms": 4500.0, "html_size_kb": 90.0,
        "has_ssl": False, "broken_links_count": 5, "seo_score": 20, "priority": "P0",
    },
]


def test_csv_file_is_created():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name
    generate_csv_report(SAMPLE_AUDITS, path)
    assert Path(path).exists()


def test_csv_has_correct_headers():
    expected = {
        "client_id", "url", "scan_date", "status_code", "title", "title_length",
        "has_description", "description_length", "has_h1", "h1_text", "ttfb_ms",
        "html_size_kb", "has_ssl", "broken_links_count", "seo_score", "priority",
    }
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False, mode="w") as f:
        path = f.name
    generate_csv_report(SAMPLE_AUDITS, path)
    with open(path, encoding="utf-8-sig") as f:
        headers = set(csv.DictReader(f).fieldnames or [])
    assert expected == headers


def test_csv_row_count():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False, mode="w") as f:
        path = f.name
    generate_csv_report(SAMPLE_AUDITS, path)
    with open(path, encoding="utf-8-sig") as f:
        assert len(list(csv.DictReader(f))) == len(SAMPLE_AUDITS)


def test_csv_score_values():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False, mode="w") as f:
        path = f.name
    generate_csv_report(SAMPLE_AUDITS, path)
    with open(path, encoding="utf-8-sig") as f:
        scores = [int(r["seo_score"]) for r in csv.DictReader(f)]
    assert scores == [85, 20]


def test_csv_empty_input():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False, mode="w") as f:
        path = f.name
    generate_csv_report([], path)
    with open(path, encoding="utf-8-sig") as f:
        assert list(csv.DictReader(f)) == []
