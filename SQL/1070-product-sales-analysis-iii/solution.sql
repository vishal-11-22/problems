# Write your MySQL query statement below
with solve as
(
    select product_id , year as first_year , quantity ,price , dense_rank() over(partition by product_id order by year) as rn
    from Sales

)
select product_id,first_year,quantity,price
from solve
where rn=1;