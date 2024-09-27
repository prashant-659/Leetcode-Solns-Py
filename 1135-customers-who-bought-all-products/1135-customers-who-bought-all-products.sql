-- -- # Write your MySQL query statement below
select customer_id from customer
group by customer_id
having count(distinct(product_key))=(select count(*) from product)
-- # Write your MySQL query statement below
-- SELECT c.customer_id
-- FROM Customer c
-- LEFT JOIN Product p ON c.product_key = p.product_key
-- GROUP BY c.customer_id
-- HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(*) FROM Product)