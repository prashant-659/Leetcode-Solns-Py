-- # Write your MySQL query statement below
# Write your MySQL query statement below
with cte as
(
    select player_id,event_date,
    rank() over(partition by player_id order by event_date) as ordered
    from activity
)
select round(sum(case
        when a2.event_date=date_add(a1.event_date, INTERVAL 1 DAY) THEN 1 ELSE 0 END)/COUNT(DISTINCT a1.player_id)   
        ,2)  as fraction

from cte a1
left join cte a2
on a1.player_id=a2.player_id 
and a1.ordered=1
and a2.ordered=2;
