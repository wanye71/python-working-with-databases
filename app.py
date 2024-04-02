import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# Filtering records in an SQLite database
release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())

connection.commit()
connection.close()