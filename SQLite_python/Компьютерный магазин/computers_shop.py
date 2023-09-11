import sqlite3


with sqlite3.connect("shopIT.db") as con:
	cur = con.cursor()

	cur.execute('''
		CREATE TABLE IF NOT EXISTS `computers` (
			`id`	INTEGER NOT NULL,
			`type`	TEXT,
			`brand`	TEXT,
			`price`	INTEGER,
			PRIMARY KEY(`id` AUTOINCREMENT)
		);
	''')

	cur.execute('''
		INSERT INTO `computers` (`type`, `brand`, `price`) VALUES
			('Thin_client', 'Tonk', 55000),
			('Desktop', 'Asrock', 28785),
			('Monoblock', 'Aquarius', 93000),
			('Notebook', 'Asus', 62990),
			('Microcomputer', 'Geekom', 67800),
			('Tablet_computer', 'Huawei', 9898),
			('Tablet_computer', 'Apple', 68990),
			('Tablet_computer', 'Honor', 22999),
			('Notebook', 'Dell', 114490),
			('Notebook', 'hP', 43999),
			('Notebook', 'MSI', 47699),
			('Desktop', 'Hp', 20428),
			('Monoblock', 'HP', 39500),
			('Notebook', 'Oloey', 19730),
			('Monoblock', 'Rombica', 76575),
			('Monoblock', 'Dell', 133320),
			('Notebook', 'Asus', 28650),
			('Monoblock', 'hp', 19990),
			('Desktop', 'HP', 75852),
			('Desktop', 'Dexp', 15999), 
			('Microcomputer', 'Rombica', 18999),
			('Desktop', 'MSI', 21999),
			('Notebook', 'Lenovo', 25810),
			('Microcomputer', 'Raspberry', 15990),
			('Microcomputer', 'Maibenben', 12500),
			('Thin_client', 'HP', 14000),
			('Thin_client', 'Dell', 5000),
			('Thin_client', 'GigaByte', 2500),
			('Notebook', 'Fplus', 29900)
		;
	''')

	# Показать все компьютеры бренда "HP"
	res = cur.execute('''
		SELECT * FROM `computers` WHERE UPPER(`brand`) = 'HP';
	''').fetchall()
	print('\nВсе компьютеры бренда "HP":')
	for x in res:
		print(x)
	print('\n------------------------------------------------------------\n')

	# Показать компьютеры стоимость которых более 40000
	res = cur.execute('''
		SELECT * FROM `computers` WHERE `price` > 40000;
	''').fetchall()
	print('Компьютеры стоимость которых более 40000:')
	for x in res:
		print(x)
	print('\n------------------------------------------------------------\n')

	# Показать компьютеры типа “ноутбук” и стоимостью менее 30000
	res = cur.execute('''
		SELECT * FROM `computers` WHERE `type` = 'Notebook' AND `price` < 30000;
	''').fetchall()
	print('Компьютеры типа “ноутбук” и стоимостью менее 30000:')
	for x in res:
		print(x)
