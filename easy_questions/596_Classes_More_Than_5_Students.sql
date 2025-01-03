# Write your MySQL query statement below
with counts as (
    select
        class,
        count(student) as student_count
    from Courses
    group by class
)
select 
    class
from counts
where student_count >= 5;

select class
from Courses
group by class
having count(student) >= 5;

