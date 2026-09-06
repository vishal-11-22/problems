# Write your MySQL query statement belo
update Salary
set 
    sex=case when sex like 'm' then 'f' else 'm' end
    