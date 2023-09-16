import sqlite3


def convert_to_binary_data(filename: str) -> bytes:
    """
        Get the path to the picture and
        return an array of bytes
    """
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


with sqlite3.connect("sales.db") as con:
	cur = con.cursor()
	
	sqlite_query = '''CREATE TABLE IF NOT EXISTS Salespeople (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			sname TEXT,
			city TEXT,
            comm INTEGER,
			avatar BLOB);
      
            CREATE TABLE IF NOT EXISTS Customers (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            cname TEXT,
			city TEXT,
			rating INTEGER,
			avatar BLOB,
		    id_sp INTEGER,
            FOREIGN KEY (id_sp) REFERENCES Salespeople(id));'''

	cur.executescript(sqlite_query)
	
	print('\nПродавцы') 
	for i in range(3):
		_sname = input('Введите фамилию: ')
		_city = input('Укажите город: ')
		_comm = int(input('Укажите размер комиссионных: '))
		_ava = convert_to_binary_data(input('Укажите путь к аватарке: '))
		cur.execute(
            "INSERT INTO Salespeople (sname, city, comm, avatar) VALUES\
            (?, ?, ?, ?);", (_sname, _city, _comm, _ava)
        )
		print('')  
		
	print('Заказчики')         
	for i in range(2):
		_cname = input('Введите фамилию: ')
		_city = input('Укажите город: ')
		_rating = int(input('Укажите рейтинг: '))
		_saler = int(input('Укажите ID продавца: '))
		_ava = convert_to_binary_data(input('Укажите путь к аватарке: '))
		cur.execute(
            "INSERT INTO Customers (cname, city, rating, avatar, id_sp) VALUES\
            (?, ?, ?, ?, ?);", (_cname, _city, _rating, _ava, _saler)
        )
		print('')
