# Write your MySQL query statement below
Select a.user_id, round(ifnull(avg(b.action='confirmed'),0),2) as confirmation_rate
from signups  a 
left join confirmations b
on a.user_id=b.user_id
group by a.user_id;