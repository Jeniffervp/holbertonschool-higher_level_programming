-- max temperature in states
SELECT state, MAX(value) 'max_temp' FROM temperatures GROUP BY state
       ORDER BY state ASC LIMIT 3;
