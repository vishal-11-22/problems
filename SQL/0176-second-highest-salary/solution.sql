# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
from Employee
where salary<(select max(salary) from employee);