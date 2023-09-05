CREATE DATABASE homestead;

USE homestead;

CREATE TABLE `gardens`(
  `id` INT NOT NULL PRIMARY KEY,
  `garden` VARCHAR(45)
);

CREATE TABLE `products` (
	`prod_id` INT,
    `product` VARCHAR(45),
	FOREIGN KEY (prod_id) REFERENCES gardens (id)
);
