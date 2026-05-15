-- Проект 7: Объединение таблиц (JOIN)

-- Таблица категорий
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT,
    priority INTEGER
);

INSERT INTO categories VALUES
(1, 'Смартфоны', 1),
(2, 'Ноутбуки', 2),
(3, 'Аксессуары', 3);

-- Таблица страниц с категориями
CREATE TABLE pages_with_category (
    page_id INTEGER,
    category_id INTEGER,
    url TEXT
);

INSERT INTO pages_with_category VALUES
(1, 1, 'https://shop.com/iphone-15'),
(2, 1, 'https://shop.com/samsung-s24'),
(3, 2, 'https://shop.com/macbook'),
(4, 3, 'https://shop.com/case');

-- JOIN: страницы + категории + метрики
SELECT 
    pwc.url,
    c.name as category,
    c.priority,
    sp.clicks,
    sp.impressions,
    ROUND(sp.clicks * 100.0 / sp.impressions, 2) as ctr
FROM pages_with_category pwc
JOIN categories c ON pwc.category_id = c.id
JOIN seo_pages sp ON pwc.url = sp.url
ORDER BY c.priority, sp.clicks DESC;

-- Агрегация по категориям
SELECT 
    c.name as category,
    COUNT(*) as pages_count,
    SUM(sp.clicks) as total_clicks,
    ROUND(AVG(sp.clicks * 100.0 / sp.impressions), 2) as avg_ctr
FROM pages_with_category pwc
JOIN categories c ON pwc.category_id = c.id
JOIN seo_pages sp ON pwc.url = sp.url
GROUP BY c.name
ORDER BY total_clicks DESC;
