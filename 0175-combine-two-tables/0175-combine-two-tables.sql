# Write your MySQL query statement below
select a.firstname as firstName,a.lastname as lastName,b.city,b.state
from person a
left join address b
on a.personId=b.personId