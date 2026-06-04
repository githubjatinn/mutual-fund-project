-- Top 5 funds by number of records
SELECT scheme_name, COUNT(*) as total_records
FROM Axis_Bluechip
GROUP BY scheme_name
ORDER BY total_records DESC
LIMIT 5;

-- Average NAV per scheme
SELECT scheme_name, ROUND(AVG(nav), 2) as avg_nav
FROM HDFC_Top100_Direct
GROUP BY scheme_name;

-- Latest NAV for each scheme
SELECT scheme_name, date, nav
FROM SBI_Bluechip
ORDER BY date DESC
LIMIT 5;