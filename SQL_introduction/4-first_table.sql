-- script that creates a table called first_table in the current database in your MySQL server.
-- If the table first_table already exists, your script should not fail

USE hbtn_0c_0;
-- creates a table called first_table in the current database in MySQL server.

CREATE table if not exists first_table(
    id INT NOT NULL,
    name VARCHAR (256) NOT NULL,
    PRIMARY KEY (id)
);