Select d.name as department , e1.name as employee, e1.salary as Salary
From Employee e1 
join Department d 
on e1.DepartmentId = d.Id
Where  3 > (select count(distinct (e2.Salary))
            from  Employee e2
            where e2.Salary > e1.Salary
            and e1.DepartmentId = e2.DepartmentId)


-- Get info on employee whose salary is not higher than 3 other peoples
-- 185_Department_Top_Three_Salaries.sql
