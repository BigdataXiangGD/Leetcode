# Write your MySQL query statement below

select Max(salary) 
as secondhighestsalary
from employee 
where salary < (select Max(Salary) from Employee)


/*找到找到最大值，然后我们取比最大值小一点的最大值。

SQL：

SELECT Max(Salary) as SecondHighestSalary FROM Employee WHERE Salary< ( SELECT  Max(Salary) FROM Employee);
 

 Max()函数表示返回最大值，如果没有则返回NULL。

Salary<( SELECT Max(Salary) FROM Employee) 则是子查询的概念。

例如 Select * From Table_A Where key in (a,b);  如果其中(a,b)的数据来源于Table_B或者Table_A表。
我们就可以使用子查询，将(a,b)的数据替换为我们查询到的数据。

Select * From Table_A Where key in (Select a,b From Table_B  Where Inr='XXXXXXX');

“as XXX”则表示将输出的数据以“XXX”为别名的方式输出。

https://www.cnblogs.com/contixue/p/7057025.html */
