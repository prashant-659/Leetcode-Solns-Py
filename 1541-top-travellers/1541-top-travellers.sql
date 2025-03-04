# Write your MySQL query statement below
with cte as(
select u.id, ifnull(sum(r.distance),0) as travelled_distance 
from users u
left outer join rides r
on u.id=r.user_id
group by u.id)
select u.name, c.travelled_distance from 
users u left join cte c
on u.id=c.id
order by travelled_distance desc, u.name;