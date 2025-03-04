# Write your MySQL query statement below
with unitscost as ( 
    select p.product_id, sum(u.units) as total_units,sum(p.price*u.units) as total_price
from prices p
left join unitssold u
on p.product_id=u.product_id
and u.purchase_date between p.start_date and p.end_Date
group by p.product_id)
select product_id, ifnull(round(total_price/total_units,2),0) as average_price
from unitscost

-- WITH unitscost AS ( 
--     SELECT p.product_id, 
--            SUM(u.units) AS total_units, 
--            SUM(p.price * u.units) AS total_price
--     FROM prices p
--     LEFT JOIN unitssold u ON p.product_id = u.product_id
--     AND u.purchase_date BETWEEN p.start_date AND p.end_date
--     GROUP BY p.product_id
-- )
-- SELECT product_id, 
--        ROUND(total_price / total_units, 2) AS average_price
-- FROM unitscost;

