# Write your MySQL query statement below
select distinct One.num as ConsecutiveNums
from Logs One
join Logs Two on One.num = Two.num
join Logs Three on Three.num = Two.num
where One.id + 1 = Two.id and Two.id + 1 = Three.id;



# Write your MySQL query statement below
# Write your MySQL query statement below
with cte as (
    select num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    from logs

)

select distinct num ConsecutiveNums 
from cte 
where (num=num1) and (num=num2)

