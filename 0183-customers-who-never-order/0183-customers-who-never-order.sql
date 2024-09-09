# Write your MySQL query statement below
-- select name as customers from customers
-- where id not in (
--     select customerId 
--     from orders
-- )

select a.name as Customers from customers a
left join orders b on
a.id=b.customerId 
where b.customerId is null;