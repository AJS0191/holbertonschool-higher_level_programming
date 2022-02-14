-- lists records with a score that is >= 10
-- list the records
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
