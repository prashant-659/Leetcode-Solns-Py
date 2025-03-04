# Write your MySQL query statement below
with cte as(
Select 
    teacher_id, count(distinct subject_id) as cnt
    from teacher
    group by teacher_id
    )
Select *
from cte
