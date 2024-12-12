# Write your MySQL query statement below

#Group by machine id

#figure out different between start and end time for each process

#Average out those times for the machine

with activity_start_end as (
    select 
        A1.machine_id,
        A1.process_id,
        A2.timestamp - A1.timestamp as duration
    from Activity A1
    join Activity A2
        on A1.machine_id = A2.machine_id
        and A1.process_id = A2.process_id
    where A1.activity_type = 'start'
        and A2.activity_type = 'end'
)
select 
    machine_id, 
    round(avg(duration),3) as processing_time
from activity_start_end ase
group by machine_id;