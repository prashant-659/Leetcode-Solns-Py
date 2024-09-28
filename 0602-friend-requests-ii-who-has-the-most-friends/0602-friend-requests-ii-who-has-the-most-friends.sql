# Write your MySQL query statement below
with cte as (
    select requester_id,accepter_id,accept_date
    from  RequestAccepted
    union all
    select accepter_id,requester_id,accept_date
    from  RequestAccepted
), 
cte2 as(
    select requester_id, count(*) as cnt from cte
    group by requester_id
)
select requester_id as id, cnt as num
from cte2 
where cnt= (select max(cnt) from cte2)