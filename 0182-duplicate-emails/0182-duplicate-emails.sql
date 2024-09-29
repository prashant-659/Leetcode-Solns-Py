# Write your MySQL query statement below
-- select email from person
-- group by email
-- having count(*)>1

with cte as(
    select email,
    row_number() over(partition by email) as rnk
    from person
)
select distinct email from cte 
where rnk>1