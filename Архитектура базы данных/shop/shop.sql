CREATE DATABASE shop;

USE shop;

CREATE TABLE `products`(
  `id` INT NOT NULL PRIMARY KEY,
  `product` VARCHAR(45)
);

CREATE TABLE `providers` (
	`prod_id` INT,
    `provider` VARCHAR(45),
	FOREIGN KEY (prod_id) REFERENCES products (id)
);
