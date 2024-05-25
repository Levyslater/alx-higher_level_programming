-- Creates a database if it already does not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates a table if it already does not exist with a column that is uunique, primary key and autogenerated
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
