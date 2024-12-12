select e.name, b.bonus
from Employee e
left join Bonus g
on e.empId = b.empId
where
b.bonus is null
or b.bonus < 1000;