CREATE DATABASE IF NOT EXISTS human_resources;

USE human_resources;

CREATE TABLE IF NOT EXISTS items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description VARCHAR(255) NOT NULL
);

INSERT INTO items (name, description) VALUES
  ('Crew Driver', 'The crew driver is the heart of the ship. It is the only thing that can hold the crew together.'),
  ('Hammer', 'A hammer is a tool that can be used to hammer things.'),
  ('Sail', 'The sail is a piece of fabric that is used to hold the crew together.');
