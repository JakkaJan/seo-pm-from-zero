-- Проект 2: Анализ CTR по страницам

-- Базовый CTR
SELECT 
    url,
    clicks,
    impressions,
    ROUND((clicks * 100.0 / impressions), 2) as ctr_percent
FROM seo_pages
ORDER BY ctr_percent DESC;

-- CTR по диапазонам позиций
SELECT 
    CASE 
        WHEN position <= 3 THEN 'Топ-3'
        WHEN position <= 10 THEN 'Топ-10'
        WHEN position <= 20 THEN 'Топ-20'
        ELSE 'За пределами 20'
    END as position_group,
    COUNT(*) as pages_count,
    ROUND(AVG(clicks * 100.0 / impressions), 2) as avg_ctr
FROM seo_pages
GROUP BY position_group
ORDER BY avg_ctr DESC;

-- Страницы с CTR ниже среднего (проблемные)
WITH avg_ctr AS (
    SELECT AVG(clicks * 100.0 / impressions) as global_avg
    FROM seo_pages
)
SELECT 
    sp.url,
    sp.title,
    ROUND((sp.clicks * 100.0 / sp.impressions), 2) as ctr,
    ROUND(a.global_avg, 2) as benchmark,
    'Низкий CTR' as status
FROM seo_pages sp, avg_ctr a
WHERE (sp.clicks * 100.0 / sp.impressions) < a.global_avg;
