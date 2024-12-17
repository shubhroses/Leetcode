# Write your MySQL query statement below
-- with user_action_count as (
--     select 
--         S.user_id, 
--         C.action, 
--         count(S.user_id) as count
--     from Signups S
--     left join Confirmations C
--     on S.user_id = C.user_id
--     group by C.action, S.user_id
-- )
-- select 
--     C.user_id, 
--     C.action, 
--     T.action
-- from user_action_count C
-- left join user_action_count T
-- on T.user_id = C.user_id
-- where C.action = 'confirmed';

# Write your MySQL query statement below
select 
    s.user_id, 
    round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s 
left join Confirmations as c 
    on s.user_id = c.user_id 
group by user_id;

