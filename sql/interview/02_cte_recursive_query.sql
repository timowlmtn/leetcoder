-- A) Simple CTE for clarity: top 3 salaries per dept
WITH dept_top3 AS (
  SELECT
    dept,
    employee,
    salary,
    ROW_NUMBER() OVER (
      PARTITION BY dept
      ORDER BY salary DESC
    ) AS rnk
  FROM employees
)
SELECT dept, employee, salary
FROM dept_top3
WHERE rnk <= 3;

-- B) Recursive CTE: traverse org hierarchy
WITH RECURSIVE org_chart AS (
  -- anchor: the CEO
  SELECT
    emp_id,
    manager_id,
    name,
    1 AS level
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  -- recursive step: find direct reports
  SELECT
    e.emp_id,
    e.manager_id,
    e.name,
    oc.level + 1
  FROM employees AS e
  JOIN org_chart AS oc
    ON e.manager_id = oc.emp_id
)
SELECT *
FROM org_chart
ORDER BY level, name;
