-- A) Rank students by score within each class
SELECT
  class_id,
  student_name,
  score,
  RANK() OVER (
    PARTITION BY class_id
    ORDER BY score DESC
  ) AS class_rank
FROM exam_results;

-- B) Compute a 3-row moving average of sales by date
SELECT
  sale_date,
  sales_amount,
  AVG(sales_amount) OVER (
    ORDER BY sale_date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS moving_avg_3day
FROM daily_sales
ORDER BY sale_date;

-- C) Show cumulative sum per department
SELECT
  dept,
  employee,
  salary,
  SUM(salary) OVER (
    PARTITION BY dept
    ORDER BY employee
    ROWS UNBOUNDED PRECEDING
  ) AS cum_salary
FROM employees;
