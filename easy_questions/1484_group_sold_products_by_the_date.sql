select sell_date, count( DISTINCT product ) as num_sold ,
    
    GROUP_CONCAT( DISTINCT product order by product ASC separator ',' ) as products
    
        FROM Activities GROUP BY sell_date order by sell_date ASC;



select 
    sell_date, 
    count(distinct product) as num_sold,
    group_concat(distinct product order by product asc separator ',') as products
from Activities
group by sell_date
order by sell_date asc;