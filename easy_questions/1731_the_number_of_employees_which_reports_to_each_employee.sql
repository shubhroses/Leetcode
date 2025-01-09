# Write your MySQL query statement below
select 
    m.employee_id,
    m.name,
    count(e.employee_id) as reports_count,
    round(avg(e.age), 0) as average_age
from Employees m
join Employees e
on e.reports_to = m.employee_id
group by m.employee_id, m.name
order by m.employee_id;

# 1731_the_number_of_employees_which_reports_to_each_employee.sql
# Dont forget to change names of columns to those question asks, read whole question to remember order by 
