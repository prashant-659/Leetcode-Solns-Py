# Write your MySQL query statement below
-- with cte as(
with cte as(
    select  departmentId,name,salary,
    rank() over(partition by departmentId order by salary desc ) as rnk
    from Employee 
    group by departmentId,name,salary
)

select b.name as Department, a.name as Employee,a.salary as Salary
    from cte a join Department b
    on a.departmentId=b.id 
    where a.rnk=1
    -- )
-- select b.department, a.name,a.salary
-- from Employee a join Department b
-- on a.departmentId=b.id 
-- group by department
-- order by a.salary desc