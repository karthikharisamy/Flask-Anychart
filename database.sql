CREATE DATABASE IF NOT EXISTS anychart_db;


 CREATE TABLE IF NOT EXISTS anychart_db.fruits (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    value INT
  );
  
  
INSERT INTO anychart_db.fruits (name, value) VALUES
      ('apples', 10),
      ('oranges', 20),
      ('bananas', 15),
      ('lemons', 5),
      ('pears', 3),
      ('apricots', 7),
      ('kiwis', 9),
      ('mangos', 12),
      ('figs', 4),
      ('limes', 8);