# Write your MySQL query statement below
with cte as(
    Select d.name as Department, e.name AS Employee, e.Salary, dense_rank() over(partition by d.name order by e.salary desc) as rankings
from employee e join department d on e.departmentid=d.id)
select Department, Employee, Salary  from cte
where rankings <=3;