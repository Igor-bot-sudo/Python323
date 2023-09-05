CREATE DATABASE cinema;

USE cinema;

CREATE TABLE `halls` (
    `id` INT NOT NULL PRIMARY KEY,
    `hall` VARCHAR(45)
);

CREATE TABLE `films`(
	`film_id` INT,
	`name` VARCHAR(45) UNIQUE,
  	FOREIGN KEY (film_id) REFERENCES halls (id)
);
