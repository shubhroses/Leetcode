# Write your MySQL query statement below
# Filter for only changes before 2018-08-17
# Group by product id and find max change date
# Select new price where change date equal that date for that product

select distinct product_id, 10 as price
from Products
group by product_id
having (min(change_date) > "2019-08-16")
union 
select p2.product_id, new_price
from Products p2
where (p2.product_id, p2.change_date) in 
(
    select product_id, max(change_date) as recent_date
    from Products
    where change_date <= "2019-08-16"
    group by product_id
)

