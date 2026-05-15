"""
test_scanner.py — тесты модуля scanner (мок HTTP-ответа).
"""
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

MOCK_HTML = """<!DOCTYPE html>
<html>
<head>
  <title>Главная страница тестового сайта</title>
  <meta name="description" content="Это тестовое описание сайта, которое точно длиннее ста двадцати символов, чтобы пройти проверку длины в нашем SEO-анализаторе.">
</head>
<body>
  <h1>Заголовок первого уровня</h1>
  <a href="/page1">Страница 1</a>
  <a href="https://external.com">Внешний</a>
  <a href="mailto:test@test.com">Email</a>
  <a href="#anchor">Якорь</a>
</body>
</html>"""


def _make_mock_response(html=MOCK_HTML, status=200, url="https://test.com"):
    mock_resp = MagicMock()
    mock_resp.status_code = status
    mock_resp.text = html
    mock_resp.content = html.encode("utf-8")
    mock_resp.url = url
    return mock_resp


def test_scan_title_parsed():
    with patch("requests.get", return_value=_make_mock_response()), \
         patch("requests.head", return_value=MagicMock(status_code=200)):
        from src.scanner import scan_site
        result = scan_site("https://test.com")
    assert result["title"] == "Главная страница тестового сайта"
    assert result["title_length"] == len("Главная страница тестового сайта")


def test_scan_meta_description_detected():
    with patch("requests.get", return_value=_make_mock_response()), \
         patch("requests.head", return_value=MagicMock(status_code=200)):
        from src.scanner import scan_site
        result = scan_site("https://test.com")
    assert result["has_description"] is True
    assert result["description_length"] > 0


def test_scan_h1_detected():
    with patch("requests.get", return_value=_make_mock_response()), \
         patch("requests.head", return_value=MagicMock(status_code=200)):
        from src.scanner import scan_site
        result = scan_site("https://test.com")
    assert result["has_h1"] is True
    assert result["h1_text"] == "Заголовок первого уровня"


def test_scan_skips_mailto_and_anchor():
    checked_urls = []
    def mock_head(url, **kwargs):
        checked_urls.append(url)
        return MagicMock(status_code=200)
    with patch("requests.get", return_value=_make_mock_response()), \
         patch("requests.head", side_effect=mock_head):
        from src.scanner import scan_site
        scan_site("https://test.com")
    assert not any("mailto" in u for u in checked_urls)
    assert not any(u.endswith("#anchor") for u in checked_urls)


def test_scan_broken_link_counted():
    html = """<html><head><title>Test Site Title OK Length</title></head>
    <body><h1>H1</h1>
    <a href="/broken1">B1</a><a href="/broken2">B2</a></body></html>"""
    def mock_head(url, **kwargs):
        return MagicMock(status_code=404)
    with patch("requests.get", return_value=_make_mock_response(html)), \
         patch("requests.head", side_effect=mock_head):
        from src.scanner import scan_site
        result = scan_site("https://test.com")
    assert result["broken_links_count"] == 2


def test_scan_timeout_returns_status_0():
    import requests as req
    with patch("requests.get", side_effect=req.exceptions.Timeout):
        from src.scanner import scan_site
        result = scan_site("https://timeout.com")
    assert result["status_code"] == 0
