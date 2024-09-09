# Write your MySQL query statement below
select employee_id, 
            IF( employee_id%2!=0 and left(name,1)<>'M', salary,0) as bonus
from employees
order by employee_id;
