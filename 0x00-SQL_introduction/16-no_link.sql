-- Displays rows with score descending and where name is not null
SELECT score, name FROM second_table WHERE name IS NOT NULL AND TRIM(name) <> '' ORDER BY score DESC;
