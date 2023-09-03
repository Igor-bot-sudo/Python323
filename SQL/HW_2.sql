USE testDB;


CREATE TABLE `Weapon` (
  `id` INT NOT NULL PRIMARY KEY,
  `Name` VARCHAR(45) NULL,
  `Type` VARCHAR(45) NULL,
  `Power` INT NOT NULL
);


INSERT INTO `Weapon` (id, Name, Type, Power) VALUES 
	(1, 'Mauser','Gun', 37),
	(2, 'Schmeiser','Machine', 56),
	(3, 'Maxim','Machine gun', 200)
;


SELECT * FROM  `Weapon` WHERE Power = 200;
