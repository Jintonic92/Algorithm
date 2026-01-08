CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

    SET N = N -1 ; #OFFSET에 변수 넣을 수 없음 
  
  RETURN (

    SELECT DISTINCT SALARY 
    FROM Employee
    ORDER BY Salary DESC
    -- LIMIT 1 OFFSET N -1
    LIMIT 1 OFFSET N

  );
END
