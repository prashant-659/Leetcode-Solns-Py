# Write your MySQL query statement below
select m.name as Employee from Employee e
join employee m on e.id=m.managerId
and  e.salary<m.salary;