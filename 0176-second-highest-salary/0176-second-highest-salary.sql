# Write your MySQL query statement below
WITH CTE AS
			(SELECT Salary, dense_rank() OVER (ORDER BY Salary desc) AS RANK_desc
			   FROM Employee)
SELECT MAX(salary) AS SecondHighestSalary
  FROM CTE
 WHERE RANK_desc = 2
