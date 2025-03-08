# Write your MySQL query statement below
with cte as (
    select *, id-row_number() over(order by id asc) as rn
    from stadium where people>=100
)
Select id, visit_date, people
from cte
where rn in (select rn from cte group by rn having count(*)>=3)
    