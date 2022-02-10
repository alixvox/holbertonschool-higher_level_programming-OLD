-- Displays the number of different scores
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score;
