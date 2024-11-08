# Write your MySQL query statement below
with cte as(
select employee_id
from employees where employee_id not in (select employee_id from salaries)
union 
select employee_id
from salaries where employee_id not in (select employee_id from employees)
)
select employee_id from cte 
order by employee_id;