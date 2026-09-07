# Write your MySQL query statement below
select id,movie,description,rating
from Cinema
where description!="boring" and MOD(id,2)=1
order by rating*-1