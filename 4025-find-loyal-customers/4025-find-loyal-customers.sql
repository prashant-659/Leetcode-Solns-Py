# Write your MySQL query statement below
-- with
With cte as(
select  
    customer_id, 
    count(transaction_id) as tran_cnt, 
    sum(case when transaction_type ='refund' then 1 
    else 0 end) as refund_ct,
    datediff(max(transaction_date),min(transaction_date )) as active
from customer_transactions
group by customer_id
)
select customer_id
from cte 
where tran_cnt>2 and active>=30 and
refund_ct/tran_cnt<0.2



