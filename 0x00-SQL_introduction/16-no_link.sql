-- shows records with names in descending order
-- select all
SELECT score, name
FROM second_table
WHERE name != NULL
ORDER BY score DESC
