# Write your MySQL query statement below
-- select m.name as Employee from Employee e
-- join employee m on e.id=m.managerId
-- and  e.salary<m.salary;

SELECT e.name as Employee
FROM Employee e
INNER JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;