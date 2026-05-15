-- Проект 3: Воронка 

CREATE TABLE traffic_funnel (
    stage TEXT PRIMARY KEY,
    users INTEGER,
    revenue REAL
);

INSERT INTO traffic_funnel VALUES
('Показы в поиске', 50000, 0),
('Клики (organic)', 2500, 0),
('Сессии на сайте', 2200, 0),
('Добавление в корзину', 350, 0),
('Оформление заказа', 120, 0),
('Оплаченный заказ', 95, 475000);

-- Воронка с конверсией
SELECT 
    stage,
    users,
    LAG(users) OVER (ORDER BY 
        CASE stage
            WHEN 'Показы в поиске' THEN 1
            WHEN 'Клики (organic)' THEN 2
            WHEN 'Сессии на сайте' THEN 3
            WHEN 'Добавление в корзину' THEN 4
            WHEN 'Оформление заказа' THEN 5
            WHEN 'Оплаченный заказ' THEN 6
        END
    ) as prev_users,
    ROUND(users * 100.0 / LAG(users) OVER (ORDER BY 
        CASE stage
            WHEN 'Показы в поиске' THEN 1
            WHEN 'Клики (organic)' THEN 2
            WHEN 'Сессии на сайте' THEN 3
            WHEN 'Добавление в корзину' THEN 4
            WHEN 'Оформление заказа' THEN 5
            WHEN 'Оплаченный заказ' THEN 6
        END
    ), 2) as conversion_rate
FROM traffic_funnel;
