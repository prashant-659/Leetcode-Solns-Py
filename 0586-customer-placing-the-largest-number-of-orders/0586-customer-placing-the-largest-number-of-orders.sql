# Write your MySQL query statement below
with cte as (select customer_number, count(order_number) as ordercount
from orders
group by customer_number)
select customer_number from cte
where ordercount=(select max(ordercount) from cte);

