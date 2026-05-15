-- Проект 5: Автоматический SEO-аудит

CREATE TABLE seo_audit (
    page_id INTEGER,
    check_date DATE,
    lcp REAL,
    fid REAL,
    cls REAL,
    title_length INTEGER,
    h1_present BOOLEAN,
    meta_description_present BOOLEAN,
    status TEXT
);

INSERT INTO seo_audit VALUES
(1, '2026-05-15', 1.5, 10, 0.01, 45, true, true, 'good'),
(2, '2026-05-15', 3.2, 25, 0.15, 72, true, false, 'needs-improvement'),
(3, '2026-05-15', 4.5, 50, 0.25, 35, false, true, 'poor'),
(4, '2026-05-15', 2.1, 15, 0.05, 58, true, true, 'good');

-- Сводка аудита
SELECT 
    status,
    COUNT(*) as pages_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percent
FROM seo_audit
GROUP BY status;

-- Проблемы, требующие исправления
SELECT 
    page_id,
    lcp,
    CASE 
        WHEN lcp > 4.0 THEN 'Критично: LCP > 4 сек'
        WHEN lcp > 2.5 THEN 'Внимание: LCP > 2.5 сек'
        ELSE 'OK'
    END as lcp_status,
    title_length,
    CASE 
        WHEN title_length > 60 THEN 'Title слишком длинный'
        WHEN title_length < 30 THEN 'Title слишком короткий'
        ELSE 'OK'
    END as title_status,
    h1_present,
    meta_description_present
FROM seo_audit
WHERE status != 'good';
