# Write your MySQL query statement below
with playerFirstDay as (
    select 
        player_id, 
        min(event_date) as first_event_date
    from Activity a
    group by player_id
),
playedSecondDay as (
    select 
        count(distinct(p.player_id)) as countValid
    from Activity a
    join playerFirstDay p
    where p.player_id = a.player_id
    and date_add(p.first_event_date, interval 1 day) = a.event_date
),
allPlayers as (
    select count(distinct(player_id)) as countAll
    from Activity
)
select round(v.countValid / a.countAll, 2) as fraction
from allPlayers a
join playedSecondDay v;


select
    round(count(disitinct player_id) / (select count(distinct player_id) from activity), 2) as fraction
from 
    Activity
where
    (player_id, date_sub(event_date, interval 1 day))
    in (
        select
            player_id, 
            min(event_date) as first_login
        from
            Activity
        group by player_id
    );

    -- 550_Game_Play_Analysis_IV.sql
