# Write your MySQL query statement below
with cte as(
    select salary,DENSE_RANK() OVER (
    ORDER BY salary DESC
  ) salary_rank
    from employee
)
select max(salary) as SecondHighestSalary  from cte where salary_rank=2;
