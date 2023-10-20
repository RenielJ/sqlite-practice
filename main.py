import sqlite3

# Connect to the database
connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE gta(release_year integer, release_name text, city text)")

release_list = [(1997, "Grand Theft Auto", "State of New Guersey"),
                (1999, "Grand Theft Auto 2", "Anywhere, USA"),
                (2001, "Grand Theft Auto III", "Liberty City"),
                (2002, "Grand Theft Auto: Vice City", "Vice City"),
                (2004, "Grand Theft Auto: San Andreas",
                 "State of San Andreas"),
                (2008, "Grand Theft Auto IV", "Liberty City"),
                (2013, "Grand Theft Auto V", "Los Santos")]

# insert the gta table
cursor.executemany("insert into gta values(?,?,?)", release_list)

for row in cursor.execute("SELECT * FROM gta"):
  print(row)

# close the data process
connection.close()
