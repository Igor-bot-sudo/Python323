import sqlite3


with sqlite3.connect('minesweeper.db') as con:
	cur = con.cursor()

	sqlite_query = '''
			CREATE TABLE IF NOT EXISTS players (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			name TEXT,
			best_score INTEGER);
	  
			CREATE TABLE IF NOT EXISTS games (
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			name TEXT,
			score INTEGER,
			id_player INTEGER,
			FOREIGN KEY (id_player) REFERENCES players(id));
			
			INSERT INTO players (name, best_score) VALUES
				('Миша', 200),
				('Ваня', 154),
				('Дима', 178),
				('Коля', 210);

			INSERT INTO games (name, score, id_player) VALUES
				('Миша', 110, 1),
				('Миша', 200, 1),
				('Дима', 178, 3),
				('Коля', 10, 4),
				('Коля', 30, 4);
			'''

	cur.executescript(sqlite_query)
	
	res = cur.execute("SELECT name, sum(score) AS Full_score FROM\
				      games GROUP BY name;").fetchall()
	for x in res:
		print(x)