# Write your MySQL query statement below
Update salary
Set sex = Case
    when sex = 'm' then 'f'
    when sex = 'f' then 'm'
END;