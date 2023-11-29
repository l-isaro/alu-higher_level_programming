-- looks for citiwa in california

SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id IN(SELECT id FROM cities)
