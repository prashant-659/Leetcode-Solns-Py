# Write your MySQL query statement below
-- select e1.name FROM employee e1 
-- join
-- ( 
--     select managerId, count(*) as directreports
--     from employee
--     group by managerId
--     having count(*)>=5
-- ) e2 on e1.id=e2.managerId;

-- select e.name from
-- employee as e
-- inner join employee as m
-- on e.id=m.managerId
-- group by m.managerId 
-- having count(m.managerId)>=5;

-- SELECT name 
-- FROM Employee 
-- WHERE id IN (
--     SELECT managerId 
--     FROM Employee 
--     GROUP BY managerId 
--     HAVING COUNT(*) >= 5)

SELECT a.name 
FROM Employee a 
JOIN Employee b ON a.id = b.managerId 
GROUP BY b.managerId 
HAVING COUNT(*) >= 5

