# Write your MySQL query statement below
Select c.name as customers
From Customers c
Left Join orders o on c.id = o.customerId
Where o.customerId is null
