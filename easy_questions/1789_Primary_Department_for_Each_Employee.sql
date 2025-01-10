# Write your MySQL query statement below
# Group by employee_id, when count department_id is 1 then just return that department employee_id
# But when count is more, return department_id where primary flat is Y

with singleDepartment as (
    select 
        employee_id,
        department_id
    from Employee e
    group by employee_id
    having count(department_id) = 1 
),
multipleDepartment as (
    select
        employee_id,
        department_id
    from Employee e
    where primary_flag = 'Y'
)
select *
from singleDepartment
union all
select *
from multipleDepartment;

-- 1789_Primary_Department_for_Each_Employee.sql
