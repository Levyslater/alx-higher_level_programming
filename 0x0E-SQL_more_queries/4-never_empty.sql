-- Creates a table if it does't already exist and sets default value to id column
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256));
