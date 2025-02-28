# Write your MySQL query statement below
with valid_sold as (
    select p.product_name, o.product_id, o.unit
    from Orders o
    join Products p
    on p.product_id = o.product_id
    where month(order_date) = '2' and year(order_date) = '2020'
)
,
tot_sold as (
    select v.product_name, v.product_id, sum(v.unit) as sold_in_feb
    from valid_sold v
    group by v.product_id, product_name
)
select product_name, sold_in_feb as unit
from tot_sold t
where t.sold_in_feb >= 100;
