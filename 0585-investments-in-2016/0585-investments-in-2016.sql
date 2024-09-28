# Write your MySQL query statement belo
select round(sum(tiv_2016),2) as tiv_2016 
from (
    select tiv_2016,
    count(*) over(partition by tiv_2015) as cnt_same_tiv_2015,
    count(*) over(partition by lat,lon) as cnt_same_lat_lon
    from insurance
) as sq
where cnt_same_tiv_2015>1 and cnt_same_lat_lon=1;

