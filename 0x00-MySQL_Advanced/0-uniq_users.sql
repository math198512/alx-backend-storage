-- Write a SQL script that creates a table users 
-- with a id, email, and name columns.
CREATE table IF NOT EXISTS users (
    id INT NOT NULL AUTO-INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    name VARCHAR(255)
);