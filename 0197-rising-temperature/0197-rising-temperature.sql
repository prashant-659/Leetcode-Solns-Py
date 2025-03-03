# Write your MySQL query statement below
with cte as(
select id, 
    recorddate,
    temperature,
    lag(recordDate) over(order by recordDate) as yesterday,  
    lag(temperature) over(
        order by recordDate
    ) as previous_temp
from weather)
select id from cte where temperature > previous_temp and datediff(recorddate, yesterday)=1;