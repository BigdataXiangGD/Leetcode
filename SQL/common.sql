/*1. return employee record with highest salary*/
select *
from employee
where salary = (select Max(salary) from employee)

/*2. select the highest salary in the employee table*/
select Max(salary) from employee

/*3. select second highest salary from employee*/
select Max(salary) 
from employee 
where salary not in (select Max(salary) from employee)
