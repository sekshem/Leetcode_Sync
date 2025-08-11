# Write your MySQL query statement below
Select 
    employee_id,
    CASE
        When(employee_id%2=1)AND(LEFT(name,1)!='M')
        THEN Salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id
