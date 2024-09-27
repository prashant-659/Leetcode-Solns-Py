# Write your MySQL query statement below
-- with cte as (
    
select person_name from (
select person_id, person_name , weight , turn,
        sum(weight) over(order by turn) as running_total
from queue) rn
where running_total<=1000
order by running_total desc
limit 1;
