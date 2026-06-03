SELECT *
FROM aum_by_fund_house
ORDER BY aum DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM nav_history;

-- 3. Average NAV by Month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month;

-- 4. SIP Transactions Count
SELECT COUNT(*)
FROM investor_transactions
WHERE transaction_type='SIP';

-- 5. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 6. Funds with Expense Ratio < 1%
SELECT *
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 7. Category-wise Fund Count
SELECT category, COUNT(*) AS fund_count
FROM fund_master
GROUP BY category;

-- 8. Fund House-wise Fund Count
SELECT fund_house, COUNT(*) AS fund_count
FROM fund_master
GROUP BY fund_house
ORDER BY fund_count DESC;

-- 9. Top 10 Funds by 5-Year Return
SELECT *
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 10. Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM scheme_performance;