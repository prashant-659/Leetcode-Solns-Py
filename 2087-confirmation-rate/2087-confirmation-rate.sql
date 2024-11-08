# Write your MySQL query statement below
-- Select a.user_id, round(ifnull(avg(b.action='confirmed'),0),2) as confirmation_rate
-- from signups  a 
-- left join confirmations b
-- on a.user_id=b.user_id
-- group by a.user_id;

-- With cte as 
-- (
--     select s.user_id, count(*) as total,
--             sum(case when action='confirmed' then 1 else 0 end ) as confirmed
--             from signups s 
--             left join confirmations c
--             on s.user_id=c.user_id
--             group by s.user_id
--             )
-- select user_id, round(confirmed/total,2) as confirmation_rate
-- from cte;


with cte as(
    select s.user_id, count(*) as total,
                    sum(case when c.action="confirmed" then 1 else 0 end) as confs
    from signups s left join confirmations c on s.user_id=c.user_id
    group by s.user_id

)
select user_id, round((confs/total),2) as confirmation_rate from cte;




