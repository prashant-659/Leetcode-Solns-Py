CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT(salary) from (
        select salary, dense_rank() over(order by salary desc) as 'Rank'
        from employee
      ) p
      where p.Rank=N
      
  );
END

#pls upvote if you find solution easy to undestand....!! Thanks..!!!