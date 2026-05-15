"""
scanner.py — сканирование сайтов: HTTP-метрики, meta-теги, битые ссылки.
"""
import time
import logging
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
import yaml

logger = logging.getLogger(__name__)

_SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "#")


def _load_config() -> dict:
    with open("config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def scan_site(url: str) -> dict:
    """Сканирует сайт и возвращает словарь с SEO-метриками."""
    cfg = _load_config()
    scanner_cfg = cfg.get("scanner", {})
    timeout = scanner_cfg.get("timeout", 10)
    user_agent = scanner_cfg.get("user_agent", "Mozilla/5.0 (compatible; DELTA-SEO-Bot/1.0)")
    max_links = scanner_cfg.get("max_links_to_check", 20)

    headers = {"User-Agent": user_agent}
    result = {
        "url": url,
        "status_code": None,
        "title": None,
        "title_length": 0,
        "has_description": False,
        "description_length": 0,
        "has_h1": False,
        "h1_text": None,
        "ttfb_ms": None,
        "html_size_kb": 0.0,
        "has_ssl": url.startswith("https://"),
        "broken_links_count": 0,
        "scan_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    try:
        t0 = time.monotonic()
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        ttfb = (time.monotonic() - t0) * 1000

        result["status_code"] = response.status_code
        result["ttfb_ms"] = round(ttfb, 1)
        result["html_size_kb"] = round(len(response.content) / 1024, 2)
        result["has_ssl"] = response.url.startswith("https://")

        soup = BeautifulSoup(response.text, "html.parser")

        # Title
        title_tag = soup.find("title")
        if title_tag and title_tag.string:
            title_text = title_tag.string.strip()
            result["title"] = title_text
            result["title_length"] = len(title_text)

        # Meta description
        desc_tag = soup.find("meta", attrs={"name": lambda n: n and n.lower() == "description"})
        if desc_tag and desc_tag.get("content"):
            result["has_description"] = True
            result["description_length"] = len(desc_tag["content"].strip())

        # H1
        h1_tag = soup.find("h1")
        if h1_tag:
            result["has_h1"] = True
            result["h1_text"] = h1_tag.get_text(strip=True)[:200]

        # Битые ссылки
        anchors = soup.find_all("a", href=True)
        links_to_check = []
        for a in anchors:
            href = a["href"].strip()
            if not href or any(href.startswith(s) for s in _SKIP_SCHEMES):
                continue
            abs_url = urljoin(url, href)
            parsed = urlparse(abs_url)
            if parsed.scheme not in ("http", "https"):
                continue
            links_to_check.append(abs_url)
            if len(links_to_check) >= max_links:
                break

        broken = 0
        for link in links_to_check:
            try:
                r = requests.head(link, headers=headers, timeout=timeout, allow_redirects=True)
                if r.status_code >= 400:
                    broken += 1
                    logger.debug("Broken link %s -> %d", link, r.status_code)
            except Exception as e:
                broken += 1
                logger.debug("Link error %s: %s", link, e)

        result["broken_links_count"] = broken
        logger.info("Scanned %s: ttfb=%.0f ms, broken=%d", url, ttfb, broken)

    except requests.exceptions.Timeout:
        logger.warning("Timeout scanning %s", url)
        result["status_code"] = 0
    except requests.exceptions.SSLError:
        logger.warning("SSL error for %s", url)
        result["status_code"] = 0
        result["has_ssl"] = False
    except Exception as e:
        logger.error("Error scanning %s: %s", url, e)
        result["status_code"] = 0

    return result
