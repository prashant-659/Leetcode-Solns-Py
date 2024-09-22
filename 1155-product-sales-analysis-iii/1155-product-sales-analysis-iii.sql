# Write your MySQL query statement below
-- with cte as
-- (
--     select sale_id,product_id, year,quantity, price,
--     row_number() over(partition by product_id order by year asc) as first_year
--     from sales
-- )
-- select p.product_id, c.year as first_year,c.quantity, c.price
-- from cte c
-- inner join product p
-- on c.product_id=p.product_id
-- where c.first_year=1;
SELECT 
  product_id, 
  year AS first_year, 
  quantity, 
  price 
FROM 
  Sales 
WHERE 
  (product_id, year) IN (
    SELECT 
      product_id, 
      MIN(year) AS year 
    FROM 
      Sales 
    GROUP BY 
      product_id
  );

