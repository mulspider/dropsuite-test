SELECT mark, COUNT(1) AS count
  from Users 
GROUP BY mark
UNION 
SELECT 'A+B' mark, SUM(case when mark != 'C' then 1 ELSE 0 END) AS count
  from Users 
UNION 
SELECT 'A+C' mark, SUM(case when mark != 'B' then 1 ELSE 0 END) AS count
  from Users 
UNION 
SELECT 'A+B+C' mark, SUM(case when mark != 'None' then 1 ELSE 0 END) AS count
  from Users 
