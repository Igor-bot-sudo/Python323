CREATE DATABASE school;

USE school;

CREATE TABLE `teachers`(
  `id` INT NOT NULL PRIMARY KEY,
  `first_name` VARCHAR(45),
  `last_name` VARCHAR(45),
  `patronymic` VARCHAR(45),
  `post` VARCHAR(45)
);

CREATE TABLE `subjects` (
	`subj_id` INT,
    `subject` VARCHAR(45),
	FOREIGN KEY (subj_id) REFERENCES teachers (id)
);
