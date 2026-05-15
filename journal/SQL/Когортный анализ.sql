-- Проект 4: Когортный анализ 'retention'

CREATE TABLE user_cohorts (
    user_id INTEGER,
    signup_date DATE,
    visit_date DATE
);

INSERT INTO user_cohorts VALUES
(1, '2026-01-01', '2026-01-01'),
(1, '2026-01-01', '2026-01-08'),
(1, '2026-01-01', '2026-01-15'),
(2, '2026-01-01', '2026-01-01'),
(2, '2026-01-01', '2026-01-08'),
(3, '2026-01-08', '2026-01-08'),
(3, '2026-01-08', '2026-01-15'),
(4, '2026-01-15', '2026-01-15');

-- Retention по неделям
SELECT 
    signup_date as cohort,
    COUNT(DISTINCT user_id) as cohort_size,
    COUNT(DISTINCT CASE WHEN visit_date = signup_date THEN user_id END) as week_0,
    COUNT(DISTINCT CASE WHEN visit_date = signup_date + 7 THEN user_id END) as week_1,
    COUNT(DISTINCT CASE WHEN visit_date = signup_date + 14 THEN user_id END) as week_2,
    ROUND(COUNT(DISTINCT CASE WHEN visit_date = signup_date + 7 THEN user_id END) * 100.0 / 
          COUNT(DISTINCT user_id), 1) as retention_w1
FROM user_cohorts
GROUP BY signup_date;
