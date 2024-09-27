# Write your MySQL query statement below
-- select person_name from (
-- select person_id, person_name , weight , turn,
--         sum(weight) over(order by turn) as running_total
-- from queue) rn
-- where running_total<=1000
-- order by running_total desc
-- limit 1;

Select q1.person_name
from queue q1 join queue q2
on q1.turn>=q2.turn
group by q1.turn
having sum(q2.weight) <=1000
order by q1.turn desc
limit 1;
