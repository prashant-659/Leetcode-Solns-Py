# Write your MySQL query statement below
-- Select e.name, b.bonus
-- from employee e 
-- left join bonus b
-- on e.empId=b.empId
-- where ifnull(b.bonus,0)<1000

SELECT
    Employee.name, Bonus.bonus
FROM
    Employee
        LEFT JOIN
    Bonus ON Employee.empid = Bonus.empid
WHERE
    bonus < 1000 OR bonus IS NULL
;