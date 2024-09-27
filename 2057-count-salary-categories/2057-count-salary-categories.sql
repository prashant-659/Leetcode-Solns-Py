# Write your MySQL query statement below

-- select (case 
--             when income<20000 then "Low income"
--             when income >=20000 or income<=50000 then "Average income"
--             when income>50000 then "High income" end) as category,
--        count(*) as accounts_count
-- from Accounts
-- group by category;
Select "Low Salary"  as category, sum(if(income<20000,1,0)) as accounts_count
from accounts
union
Select "Average Salary" as category, sum(if(income between 20000 and 50000,1,0)) as accounts_count
from accounts
union
Select "High Salary" as category, sum(if(income>50000,1,0)) as accounts_count
from accounts
