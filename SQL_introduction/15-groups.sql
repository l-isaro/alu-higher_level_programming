-- list the number of records with the same score

SELECT score, COUNT(DISTINCT score) AS number
FROM second_table
