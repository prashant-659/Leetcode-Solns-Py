# Write your MySQL query statement below
with cte as (
    select emp_id, event_day, sum(in_time) as intime, sum(out_time) as outtime
    from employees
    group by emp_id, event_Day
)
select event_day as day, emp_id, (outtime-intime) as total_time
from cte;
