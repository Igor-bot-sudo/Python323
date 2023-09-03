USE testDB;


CREATE TABLE `Group` (
  `id` INT NOT NULL PRIMARY KEY,
  `Name` VARCHAR(45) NULL,
  `Rating` INT NOT NULL,
  `Course` VARCHAR(45) NULL
);


INSERT INTO `Group` (id, Name, Rating, Course) VALUES 
	(1, 'A', 37, 'Physics'),
    (2, 'C', 56, 'Chemistry'),
    (3, 'B', 42, 'Sociology')
;


SELECT * FROM  `Group` WHERE Rating <= 50;
