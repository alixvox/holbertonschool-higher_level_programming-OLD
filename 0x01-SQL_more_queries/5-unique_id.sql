-- Creates table unique_id if not exists
CREATE TABLE IF NOT EXISTS unique_id
(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
