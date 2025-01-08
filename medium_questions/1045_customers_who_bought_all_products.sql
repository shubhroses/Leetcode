# Write your MySQL query statement below
with numDistinctProds as (
    select count(*) as numProds
    from Product
),
countProdsBoughtByCustomer as (
    select 
        customer_id,
        count(distinct product_key) as boughtProds
    from Customer 
    group by customer_id
)
select c.customer_id
from countProdsBoughtByCustomer c
join numDistinctProds p
where c.boughtProds = p.numProds;

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from Product);
