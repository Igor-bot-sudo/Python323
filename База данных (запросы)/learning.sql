CREATE DATABASE learning;

USE learning;

CREATE TABLE `groups` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45)
);

CREATE TABLE `students` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45),
	`group_id` INT,
	FOREIGN KEY (`group_id`) REFERENCES `groups`(`id`)
);

CREATE TABLE `lessons` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name_l` VARCHAR(45),
	`cabinet` INT NOT NULL
);

CREATE TABLE `shedule` (
    `date_time` VARCHAR(45),
	`id_groups` INT,
	`id_lessons` INT,
	FOREIGN KEY (`id_groups`) REFERENCES `groups`(`id`),
	FOREIGN KEY (`id_lessons`) REFERENCES `lessons`(`id`)
);

INSERT INTO `groups` (name) VALUES 
	('Mathematics_group'),
	('Statistics_group'),
	('Theoretical_physics_group'),
    ('Programming_group'),
    ('Biophysics_group'),
    ('Chemistry_group'),
	('Astronomy_group')
;

INSERT INTO `students` (name, group_id) VALUES 
	('Levashov A.M.', 1),
	('Vinokurova K.Z.', 3),
	('Korneeva A.D.', 4),
	('Afanasyev G.B.', 3),
	('Osipov V.N.', 6),
	('Lebedev F.F.', 2),
	('Komarov S.M.', 5),
	('Terehov N.V.', 2),
	('Golubev D.U.', 1),
	('Revich O.K.', 4),
	('Shapiro A.E.', 5),
	('Dafner E.U.', 1),
	('Erenburg P.M.', 6),
	('Uydin D.A.', 3),
	('Polischuk N.G.', 2),
	('Azarova M.A.', 4),
	('Bulah B.Y.', 5)
;

INSERT INTO `lessons` (name_l, cabinet) VALUES
	('Programming_Python', 1),
	('Statistics', 12),
	('Probability_theory', 9),
	('Chemistry', 34),
	('Theoretical_physics', 17),
	('Biophysics', 13),
	('Mathematics', 8),
	('Astronomy', 14)
;

INSERT INTO `shedule` (date_time, id_groups, id_lessons) VALUES
	('2023-09-12 09:00', 1, 1),
	('2023-09-12 11:00', 1, 7),
	('2023-09-12 15:00', 1, 2),
	('2023-09-12 09:00', 2, 7),
	('2023-09-12 11:00', 2, 2),
	('2023-09-12 15:00', 2, 3),
	('2023-09-12 09:00', 3, 2),
	('2023-09-12 11:00', 3, 1),
	('2023-09-12 15:00', 3, 3),
	('2023-09-12 09:00', 4, 1),
	('2023-09-12 11:00', 4, 3),
	('2023-09-12 15:00', 4, 8),
	('2023-09-13 09:00', 1, 8),
	('2023-09-13 11:00', 1, 7),
	('2023-09-13 15:00', 1, 2),
	('2023-09-13 09:00', 2, 1),
	('2023-09-13 11:00', 2, 3),
	('2023-09-13 15:00', 2, 8),
	('2023-09-13 09:00', 3, 5),
	('2023-09-13 11:00', 3, 4),
	('2023-09-13 15:00', 3, 3),
	('2023-09-13 09:00', 4, 2),
	('2023-09-13 11:00', 4, 8),
	('2023-09-13 15:00', 4, 1)
;

-- Все занятия у группы программистов
SELECT shedule.date_time, lessons.name_l AS lesson FROM shedule JOIN lessons
WHERE id_groups = (SELECT id FROM `groups` WHERE `name` = 'Programming_group') AND id_lessons = lessons.id
;

-- Все группы, которые должны быть на занятии по статистике 12.09.2023
SELECT date_time, `groups`.name FROM `shedule` JOIN `groups`
WHERE date_time LIKE '2023-09-12%' AND id_lessons = (SELECT id FROM `lessons` WHERE name_l = 'Statistics') AND id_groups = `groups`.id
ORDER BY date_time
;

-- Группа теоретической физики и ее расписание на 13.09.2023
SELECT date_time, name_l AS lesson FROM `shedule` JOIN `lessons`
WHERE date_time LIKE '2023-09-13%' AND 
id_groups = (SELECT id FROM  `groups` WHERE name = 'Theoretical_physics_group') AND `shedule`.id_lessons =  `lessons`.id
ORDER BY date_time
;
