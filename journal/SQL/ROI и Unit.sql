-- Проект 6: ROI и Unit-экономика

CREATE TABLE campaign_metrics (
    channel TEXT,
    spend REAL,
    clicks INTEGER,
    conversions INTEGER,
    revenue REAL
);

INSERT INTO campaign_metrics VALUES
('SEO Organic', 50000, 2500, 95, 475000),
('Google Ads', 120000, 8000, 240, 720000),
('Yandex Direct', 80000, 5000, 150, 450000);

-- Unit-экономика
SELECT 
    channel,
    spend,
    revenue,
    ROUND(revenue - spend, 2) as profit,
    ROUND((revenue - spend) * 100.0 / spend, 2) as roi_percent,
    ROUND(spend / clicks, 2) as cpc,
    ROUND(spend / conversions, 2) as cpa,
    ROUND(revenue / conversions, 2) as ltv,
    ROUND(conversions * 100.0 / clicks, 2) as conversion_rate
FROM campaign_metrics
ORDER BY roi_percent DESC;

-- Что если увеличить SEO-бюджет на 50%?
SELECT 
    channel,
    spend as current_spend,
    ROUND(spend * 1.5, 2) as projected_spend,
    ROUND(revenue * 1.3, 2) as projected_revenue, -- SEO имеет накопительный эффект
    ROUND((revenue * 1.3 - spend * 1.5) * 100.0 / (spend * 1.5), 2) as projected_roi
FROM campaign_metrics
WHERE channel = 'SEO Organic';
