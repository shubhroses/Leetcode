# Write your MySQL query statement below
select distinct One.num as ConsecutiveNums
from Logs One
join Logs Two on One.num = Two.num
join Logs Three on Three.num = Two.num
where One.id + 1 = Two.id and Two.id + 1 = Three.id;
