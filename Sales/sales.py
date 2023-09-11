import sqlite3


with sqlite3.connect("sales.db") as con:
	cur = con.cursor()
	
	cur.execute(
		"CREATE TABLE Salespeople (id INTEGER NOT NULL,\
			  sname TEXT, city	TEXT, comm	INTEGER,\
			  PRIMARY KEY(id AUTOINCREMENT));"
	)
	
	cur.execute(
		"CREATE TABLE Customers (id	 INTEGER NOT NULL,\
            cname	 TEXT, city	 TEXT, rating INTEGER,\
		    id_sp INTEGER, PRIMARY KEY(id AUTOINCREMENT),\
            FOREIGN KEY (id_sp) REFERENCES Salespeople(id));"
	)
       
	with open('salespeople.txt', encoding='UTF-8') as f:
		for line in f:
			_sname, _city, _comm = line.rstrip().split(',')
			cur.execute(
		      "INSERT INTO Salespeople (sname, city, comm) VALUES\
                (?, ?, ?);", (_sname, _city, int(_comm))
	        )
			
	with open('customers.txt', encoding='UTF-8') as f:
		for line in f:
			_cname, _city, _rating, _id_sp = line.rstrip().split(',')
			cur.execute(
		      "INSERT INTO Customers (cname, city, rating, id_sp) VALUES\
                (?, ?, ?, ?);", (_cname, _city, int(_rating), int(_id_sp))
	        )
