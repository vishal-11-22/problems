with clients as
(
    select * from Users where role like 'client' and banned like 'No'
), drivers as
(
    select * from Users where role like 'driver'and banned like 'No'
)
, real_trips as 
(
select * from Trips
where client_id in (select users_id from clients) and driver_id in (select users_id from drivers)
)
,grouped_trips as
(
    select request_at, count(*) as "total_trips",sum(
        case 
        when status not like 'completed' then 1 else 0
        end
    )/count(*) as "Cr"
    from real_trips
    where request_at between "2013-10-01" and "2013-10-03"
    group by request_at
)
select request_at as 'Day',ROUND(Cr,2) as "Cancellation Rate"
from grouped_trips