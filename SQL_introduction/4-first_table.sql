-- script that creates a table called first_table in the current database in your MySQL server.
-- If the table first_table already exists, your script should not fail

USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
    `id` INT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
 
);