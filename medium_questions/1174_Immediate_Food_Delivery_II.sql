# Write your MySQL query statement below
-- For each customer, find the first order and if its an immediate order
-- Get percentage of all customers that meet this criteria

with firstOrderDate as (
    select 
        customer_id, 
        min(order_date) as order_date
    from Delivery d
    group by customer_id
),
firstImmediate as (
    select 
        f.customer_id as allValid
    from firstOrderDate f
    left join Delivery d 
    on f.customer_id = d.customer_id
    and f.order_date = d.order_date   
    where f.order_date  =  d.customer_pref_delivery_date
),
allCust as (
    select 
        distinct(customer_id) as allCust
    from Delivery
)
select round(count(distinct(f.allValid))/count(distinct(a.allCust))*100, 2) as immediate_percentage
from allCust a
join firstImmediate f;


Select 
    round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);

1174_Immediate_Food_Delivery_II.sql
