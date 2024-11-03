# Write your MySQL query statement below
-- select id,
--     case when id%2=0 then (lag(student) over (order by id))
--     else ifnull(lead(student) over (order by id), student)
--     end as 'student'
--     from seat

-- select 
-- case 
-- when id=(select max(id) from seat) and id%2=1 then id
-- when id %2=1 then id+1 else id-1 end as id,   
-- student
-- from seat
-- order by id asc;





select id,
            case when id%2=0 then lag(student) over(order by id)
            else ifnull(lead(student) over(order by id), student)
            end as 'student'
        from seat;


