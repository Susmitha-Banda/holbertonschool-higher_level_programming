-- create db hbtn_0d_2 and user_0d_2, pw: user_0d_2_pwd
-- script should not fail if db or user already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
