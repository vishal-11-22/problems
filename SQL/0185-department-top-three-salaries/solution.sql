# Write your MySQL query statement below
with joined as
(
    select d.name as "Department",e.name as "Employee", e.salary as "Salary"
    from Department d
    inner join Employee e
    on d.id=e.departmentId

),
 sample as(
select j.*,dense_rank() over(partition by Department order by Salary desc) as rn
from joined j
)
select Department,Employee,Salary
from sample s 
where rn<=3;