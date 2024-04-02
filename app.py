import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
# (Title TEXT, Director TEXT, Year INT)''')
cursor.execute('''INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)''')
cursor.execute('''SELECT * FROM Movies''')

print(cursor.fetchone())

connection.commit()
connection.close()