-- create a 2nd table second_table in the db hbtn_0c_0
-- id INT, name VARCHAR(256), score INT
-- if it already exists, the script should not fail
-- not allowed to use SELECT AND SHOW


CREATE table if not exists second_table(
    id INT NOT NULL,
    name VARCHAR (256) NOT NULL,
    score INT,
    PRIMARY KEY (id)
);

-- Insert data into the table

INSERT INTO second_table(id, name, score)
VALUES 
(1, "John", 10 ),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
