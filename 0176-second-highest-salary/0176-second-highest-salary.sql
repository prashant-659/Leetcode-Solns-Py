# Write your MySQL query statement below
-- WITH CTE AS
-- 			(SELECT Salary, dense_rank() OVER (ORDER BY Salary desc) AS RANK_desc
-- 			   FROM Employee)
-- SELECT MAX(salary) AS SecondHighestSalary
--   FROM CTE
--  WHERE RANK_desc = 2

select (
    select distinct salary from employee order by salary desc limit 1 offset 1
)
as SecondHighestSalary;
