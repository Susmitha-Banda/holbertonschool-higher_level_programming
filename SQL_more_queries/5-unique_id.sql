--  creates the table unique_id on your MySQL server.
-- id INT with the default value 1 and must be unique
-- If the table unique_id already exists, your script should not fail

CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);