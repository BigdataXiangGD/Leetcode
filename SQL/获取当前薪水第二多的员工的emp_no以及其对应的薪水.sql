select employees.emp_no, max(salaries.salary), employees.last_name, employees.first_name
from employees
inner join salaries
on employees.emp_no = salaries.emp_no
where salaries.to_date = '9999-01-01' 
and salaries.salary not in (select max(salaries.salary) from salaries where salaries.to_date = '9999-01-01')


SELECT
    e.emp_no,
    max( salary ) salary,
    last_name,
    first_name
FROM
    employees e,
    salaries s
WHERE
    e.emp_no = s.emp_no
    AND to_date = '9999-01-01'
    AND salary < ( SELECT max( salary ) FROM salaries )
