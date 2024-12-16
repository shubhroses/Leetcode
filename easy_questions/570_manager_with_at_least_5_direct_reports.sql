# Write your MySQL query statement below

# Want to find distinct names which are marked as manageId for at least 5 other people

# For each individual find out all people they are marked a manager for 

# Filter for more than count of 5

# Return names


select 
    M.name
from Employee M
join Employee E
on E.managerId = M.id
group by E.managerId
having count(E.id)>= 5;


