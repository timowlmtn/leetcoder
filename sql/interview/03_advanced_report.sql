-- A) Pivot monthly sales into columns
SELECT
  region,
  SUM(CASE WHEN month = 'Jan' THEN amount END) AS Jan,
  SUM(CASE WHEN month = 'Feb' THEN amount END) AS Feb,
  SUM(CASE WHEN month = 'Mar' THEN amount END) AS Mar
FROM regional_sales
GROUP BY region;

-- B) Unpivot product-region sales (rows for each month)
SELECT region, 'Jan' AS month, jan_amt  AS amount FROM sales_pivot
UNION ALL
SELECT region, 'Feb', feb_amt FROM sales_pivot
UNION ALL
SELECT region, 'Mar', mar_amt FROM sales_pivot;

-- C) Hierarchical total: each manager’s team headcount
WITH RECURSIVE team AS (
  SELECT manager_id AS root_mgr, emp_id, 1 AS lvl
  FROM employees
  WHERE manager_id IS NOT NULL
  UNION ALL
  SELECT t.root_mgr, e.emp_id, t.lvl + 1
  FROM team AS t
  JOIN employees AS e
    ON e.manager_id = t.emp_id
)
SELECT
  root_mgr AS manager,
  COUNT(DISTINCT emp_id) AS team_size
FROM team
GROUP BY root_mgr;
