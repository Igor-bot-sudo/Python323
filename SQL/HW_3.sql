USE testDB;


CREATE TABLE `Doctors` (
  `id` INT NOT NULL PRIMARY KEY,
  `Post` VARCHAR(45) NULL,
  `Salary` INT NOT NULL
);


INSERT INTO `Doctors` (id, Post, Salary) VALUES 
	(1, 'Surgeon', 40000),
	(2, 'Therapist', 37000),
	(3, 'Dentist', 42000)
;


SELECT * FROM  `Doctors` WHERE Post = 'Surgeon';
