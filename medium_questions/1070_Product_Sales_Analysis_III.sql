# Write your MySQL query statement below
with prodSale as (
    select
        product_id,
        min(year) as first_year
    from 
        Sales
    group by product_id
)
select 
    s.product_id,
    p.first_year,
    s.quantity,
    s.price
from Sales s
join prodSale p
on s.product_id = p.product_id
and s.year = p.first_year;

