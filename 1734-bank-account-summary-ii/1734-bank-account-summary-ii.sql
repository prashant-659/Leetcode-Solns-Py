# Write your MySQL query statement below
select a.name, sum(t.amount) as balance
from users a
join transactions t
on a.account=t.account
group by a.name
having balance >10000