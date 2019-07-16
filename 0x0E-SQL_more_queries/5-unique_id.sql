-- Create a new table if not exists
-- With unique id and default to 1
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
