# Write your MySQL query statement below
select d2.id
from Weather d1
join Weather d2
on d1.recordDate = DATE_ADD(d2.recordDate, INTERVAL -1 DAY)
where d2.temperature > d1.temperature;

