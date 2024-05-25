-- Creates a table if not exist with a defaualt attribute which is also unique
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
