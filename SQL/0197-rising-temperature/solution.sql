# Write your MySQL query statement below
with cal as
(
    select id,temperature-lag(temperature) over(order by recordDate) as diff,datediff(recordDate,lag(recordDate)over(order by recordDate)) as datediffer
    from Weather
)
select id 
from cal
where diff>0 and datediffer=1;