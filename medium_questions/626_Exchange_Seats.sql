-- # Write your MySQL query statement below
with comb as (
select 
    s1.id,
    ifnull(s2.student, s1.student) as student
from Seat s1
left join Seat s2
on s1.id + 1 = s2.id
where mod(s1.id, 2) = 1

UNION

select 
    s1.id,
    ifnull(s2.student, s1.student) as student
from Seat s1
left join Seat s2
on s1.id = s2.id + 1
where mod(s1.id, 2) = 0
)
select * 
from comb
order by id;


select row_number() over() id, student
from Seat
order by if(MOD(id,2) = 0, id-1, id+1); 


-- 626_Exchange_Seats.sql

select  
    case 
    when id % 2 = 0 then id - 1
    when id % 2 = 1 and id < (select count(*) from seat) then id + 1
    else id
    end as id, 
student from seat
order by id;
