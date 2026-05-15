-- Проект 1: База данных SEO-страниц

-- Создаём таблицу
CREATE TABLE seo_pages (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL,
    title TEXT,
    h1 TEXT,
    description TEXT,
    clicks INTEGER DEFAULT 0,
    impressions INTEGER DEFAULT 0,
    position REAL,
    is_indexed BOOLEAN DEFAULT true,
    created_at DATE DEFAULT CURRENT_DATE
);

-- Добавляем тестовые данные
INSERT INTO seo_pages (url, title, clicks, impressions, position) VALUES
('https://shop.com/iphone-15', 'Купить iPhone 15', 150, 3000, 3.2),
('https://shop.com/samsung-s24', 'Купить Samsung S24', 80, 2000, 5.1),
('https://shop.com/xiaomi-14', 'Купить Xiaomi 14', 45, 1500, 8.5),
('https://shop.com/google-pixel', 'Google Pixel 8', 20, 800, 12.3),
('https://shop.com/oneplus-12', 'OnePlus 12', 15, 600, 15.7);

-- Проверяем
SELECT * FROM seo_pages;
