from pathlib import Path
import json
import sqlite3

"""
Watch Mosh's video 9.8. You will need to install
DB Browser for SQLlite and learn how to create a table
"""


# Chapter 9.8- Working with a SQLite Database
print("\n9.8- Working with a SQLite Database" + "-" * 20)

# Another way to loop through a list of dictionaries. Important for Chapter 9.8 Databases
# a json file is a text files formated similar to a python dictionary

movies = json.loads(Path("movies.json").read_text())
print(movies)
for movie in movies:
    print(movie.values())

db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "INSERT INTO Movies (Id, Title, Year) VALUES(?,?,?)"
    for movie in movies:
        movie_values = tuple(movie.values())
        conn.execute(sql_command, movie_values)
    conn.commit()
    print("Data written to the database")
