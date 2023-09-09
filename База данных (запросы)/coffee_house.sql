CREATE DATABASE coffee_house;

USE coffee_house;

CREATE TABLE `coffee` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45)
);

CREATE TABLE `barista`(
	`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`barista_name` VARCHAR(45)
);

CREATE TABLE `shift` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `shift_name` VARCHAR(45)
);


INSERT INTO `barista` (id, barista_name) VALUES 
	(1, 'Bobby'),
	(2, 'Kay'),
	(3, 'Fox')
;

---------------------------------------------------------

CREATE DATABASE coffee_house;

USE coffee_house;

CREATE TABLE `coffee` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45)
);

CREATE TABLE `barista`(
	`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	`barista_name` VARCHAR(45)
);

CREATE TABLE `work_shifts` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `shift_name` VARCHAR(45),
    `barista_id` INT,
    `coffee_id` INT,
    FOREIGN KEY (`barista_id`) REFERENCES `barista`(`id`),
    FOREIGN KEY (`coffee_id`) REFERENCES `coffee`(`id`)
);

INSERT INTO `barista` (barista_name) VALUES 
	('Bobby'),
	('Kay'),
	('Fox'),
    ('Geronimo'),
    ('Amelia')
;

INSERT INTO `coffee` (name) VALUES 
	('Arabica'),
	('Java'),
	('Espresso'),
    ('Moccachino'),
    ('Cappuccino'),
    ('Latte'),
    ('Americano')
;

INSERT INTO `work_shifts` (shift_name, barista_id, coffee_id) VALUES 
	('Morning', 5, 2),
	('Morning', 5, 7),    
 	('Morning', 5, 1),   
	('Morning', 5, 3),
	('Day', 4, 4),
    ('Day', 4, 6),
    ('Day', 4, 7),
    ('Day', 4, 1),
    ('Day', 4, 3),
    ('Day', 4, 5),
    ('Day', 4, 2),
    ('Night', 2, 4),
    ('Night', 2, 2),
    ('Night', 2, 7),
    ('Night', 2, 1),
    ('Night', 2, 5)
;

-- Какой бариста на дневной смене
SELECT DISTINCT barista_name FROM barista JOIN work_shifts WHERE shift_name = 'Day' AND barista_id = barista.id;

-- Какие кофе продали на ночной смене
SELECT coffee.name FROM coffee JOIN work_shifts WHERE shift_name = 'Night' AND coffee_id = coffee.id;

-- Какой бариста продал кофе Arabica утром
SELECT DISTINCT barista_name FROM barista JOIN work_shifts WHERE shift_name = 'Morning' AND
barista_id = barista.id AND coffee_id = (SELECT DISTINCT id FROM coffee WHERE name = 'Arabica');