CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare M int;
  set M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee order by Salary desc limit M, 1
  );
END


#limit x,y，x是从0开始。limit m,1表示第m+1条(其实就是n)开始，取1条。
