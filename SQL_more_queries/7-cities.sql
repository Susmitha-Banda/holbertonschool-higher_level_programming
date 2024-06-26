-- creates db hbtn_0d_usa and table cities
-- cities (id INT, can't be NULL, FOREIGN KEY references to id of the states table)
-- name VARCHAR256 can't be NULL
-- script shouldn't fail if db or table already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);