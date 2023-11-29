-- creates a database and table with constraints

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
id INT UNIQUE AUTO-INCREMENT PRIMARY KEY,
state_id INT NOT NULL and FOREIGN KEY REFERENCES states(id),
name VARCHAR(256) can’t be null);
