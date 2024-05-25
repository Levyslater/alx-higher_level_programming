-- Create database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user if not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Grant privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Commit changes
FLUSH PRIVILEGES;
