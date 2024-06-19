-- create db hbtn_0d_usa and table states
-- id INT, unique, auto generated, can't be null, primary key
-- script shouldn't fail if db or table already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);