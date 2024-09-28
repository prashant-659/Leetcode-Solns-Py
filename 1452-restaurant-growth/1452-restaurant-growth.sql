# Write your MySQL query statement below
with cte as(
    select distinct visited_on,
            sum(amount) over(partition by visited_on order by visited_on) As am 
            from customer
)
select  visited_on,amount, 
        round(average_amount,2)as average_amount from(
            Select visited_on,
            sum(am) over(order by visited_on rows between 6 preceding and current row) as amount,
            avg(sum(am)) over(order by visited_on rows between 6 preceding and current row) as average_amount,
            count(*) over(order by visited_on rows between 6 preceding and current row ) as cnt
            from cte
            group by visited_on
        ) l
where cnt=7
order by visited_on;
