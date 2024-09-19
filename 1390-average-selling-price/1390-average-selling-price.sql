# Write your MySQL query statement below
select p.product_id,  IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
from prices p 
left join unitsSold u 
on p.product_id=u.product_id
and u.purchase_date BETWEEN start_date AND end_date
group by p.product_id;