-- looks for citiwa in california

SELECT name
FROM cities
WHERE state_id = 1
ORDER BY id IN(SELECT id FROM cities)
