# Write your MySQL query statement below
select U.unique_id, E.name
from EmployeeUNI U
right join Employees E
on U.id = E.id;

