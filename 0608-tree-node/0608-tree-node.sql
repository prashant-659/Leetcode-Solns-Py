# Write your MySQL query statement below
select id,
        case when p_id is null then "Root" 
        when exists (SELECT 1 FROM tree t2 WHERE t2.p_id = t1.id) then "Inner"
        when not exists (SELECT 1 FROM tree t2 WHERE t2.p_id = t1.id) then "Leaf"
        end as type
    from tree t1 ;