# Write your MySQL query statement below
with joining as
(
select name,salary,departmentId 
from Employee e1
where salary=(select max(salary) from employee e2 where e1.departmentId=e2.departmentId  ))
select d.name as "Department",j.name as "Employee",j.salary as "Salary"
from department d
inner join joining j
on d.id=j.departmentId;


-- SELECT 
--     d.name AS Department,
--     e.name AS Employee,
--     e.salary AS Salary
-- FROM Employee e
-- JOIN Department d
--     ON e.departmentId = d.id
-- WHERE e.salary = (
--     SELECT MAX(e2.salary)
--     FROM Employee e2
--     WHERE e2.departmentId = e.departmentId
-- );
