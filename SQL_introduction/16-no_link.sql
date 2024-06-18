-- script that lists all records of the table second_table
-- don't list rows without a name value
-- display score and the name
-- records should be listed by descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;