-- # Write your MySQL query statement below
-- with first_order as(
--     select customer_id, min(order_date) as firstorder
--     from delivery
--     group by customer_id
-- ),
-- immediate as(
--     select d.customer_id, f.firstorder
--     from first_order f
--     join delivery d
--     on f.customer_id=d.customer_id
--     where f.firstorder=d.customer_pref_delivery_date 
-- ),
-- sele

WITH first_order AS (
    SELECT customer_id, MIN(order_date) AS firstorder
    FROM delivery
    GROUP BY customer_id
),
immediate AS (
    SELECT d.customer_id, f.firstorder
    FROM first_order f
    JOIN delivery d
    ON f.customer_id = d.customer_id
    WHERE f.firstorder = d.customer_pref_delivery_date
)

SELECT round(COUNT(*) *100/ NULLIF((SELECT COUNT(*) FROM first_order), 0),2) AS immediate_percentage 
FROM immediate;


