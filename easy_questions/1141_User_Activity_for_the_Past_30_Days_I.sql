# Write your MySQL query statement below
select 
    activity_date as day,
    count(distinct user_id) as active_users
from Activity
where 1 = 1
and activity_date > DATE_SUB(DATE('2019-07-27'), INTERVAL 30 DAY)
and activity_date <= DATE('2019-07-27')
group by activity_date;

