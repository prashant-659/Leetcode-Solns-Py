# Write your MySQL query statement below
-- SELECT distinct query_name,
--                 ROUND(
--                     (sum(rating/position)/count(query_name))
--                     ,2) as quality,
--                 Round(sum(rating from (select rating from queries where rating<3))/count(query_name),2) as poor_query_percentage 
-- From queries 
-- group by query_name

SELECT DISTINCT 
    query_name,
    ROUND(SUM(rating/position) / COUNT(query_name), 2) AS quality,
    Round(100*sum(rating<3)/count(*),2) AS poor_query_percentage
FROM 
    queries
Where query_name is not null
GROUP BY 
    query_name ;

