"""
database.py — работа с SQLite: инициализация, сохранение и чтение аудитов.
"""
import sqlite3
import logging
import yaml

logger = logging.getLogger(__name__)


def _db_path() -> str:
    with open("config.yaml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg.get("files", {}).get("database", "data/monitor.db")


def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = _get_conn()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS audits (
                id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id           TEXT,
                scan_date           TEXT,
                status_code         INTEGER,
                title               TEXT,
                title_length        INTEGER,
                has_description     BOOLEAN,
                description_length  INTEGER,
                has_h1              BOOLEAN,
                h1_text             TEXT,
                ttfb_ms             REAL,
                html_size_kb        REAL,
                has_ssl             BOOLEAN,
                broken_links_count  INTEGER,
                seo_score           INTEGER,
                priority            TEXT
            )
        """)
    conn.close()
    logger.info("Database initialised at %s", _db_path())


def save_audit(data: dict) -> None:
    conn = _get_conn()
    with conn:
        conn.execute("""
            INSERT INTO audits (
                client_id, scan_date, status_code, title, title_length,
                has_description, description_length, has_h1, h1_text,
                ttfb_ms, html_size_kb, has_ssl, broken_links_count,
                seo_score, priority
            ) VALUES (
                :client_id, :scan_date, :status_code, :title, :title_length,
                :has_description, :description_length, :has_h1, :h1_text,
                :ttfb_ms, :html_size_kb, :has_ssl, :broken_links_count,
                :seo_score, :priority
            )
        """, data)
    conn.close()


def get_last_audit(client_id: str) -> dict | None:
    conn = _get_conn()
    row = conn.execute(
        "SELECT * FROM audits WHERE client_id=? ORDER BY scan_date DESC LIMIT 1",
        (client_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def get_all_audits() -> list[dict]:
    conn = _get_conn()
    rows = conn.execute(
        "SELECT * FROM audits ORDER BY scan_date DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
