# Write your MySQL query statement below

Select visited_on,
        (
            Select sum(amount) from customer
            where visited_on between date_sub(c.visited_on, Interval 6 Day) and c.visited_on #7th jan
        ) as amount,
        Round((
            Select sum(amount)/7 from customer
            where visited_on between date_sub(c.visited_on, Interval 6 Day) and c.visited_on #7th jan
        ),2) as average_amount
From Customer c
where visited_on>=(
    Select date_add(min(visited_on), interval 6 day)
    from Customer
)
group by visited_on
order by visited_on