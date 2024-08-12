-- Write a SQL script that creates a table users 
-- with a id, email, and name columns.
CREATE table IF NOT EXISTS users (
    id INT PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255)
);