# Write your MySQL query statement below
with cte as
(
    select customer_id,delivery_id,order_date,customer_pref_delivery_date,
    row_number() over(partition by customer_id order by order_date) as firstorder
    from delivery
)
select round(
    100*sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)/count(*),2)  as immediate_percentage
from cte 
where firstorder=1;