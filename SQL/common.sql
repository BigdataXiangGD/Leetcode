/*1. return employee record with highest salary*/
select *
from employee
where salary = (select Max(salary) from employee)
