# Write your MySQL query statement below
with cte as(
    select distinct product_id, max(change_Date) over(partition by product_id) as last_day
    from products where change_Date<="2019-08-16"

)
select c.product_id, p.new_price as price
from cte c
join products p
on c.product_id=p.product_id and c.last_day=change_date

union
select product_id, 10 as price
from products
where product_id not in (select product_id from cte)