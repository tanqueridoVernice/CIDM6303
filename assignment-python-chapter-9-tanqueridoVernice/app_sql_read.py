import sqlite3

print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies"
    cursor = conn.execute(sql_command)
    for row in cursor:
        # row is a tuple
        print(f"The movie {row[1]} was released in {row[2]}")

# Modify the sql_command to filter data
# Remember your SELECT FROM WHERE statements? Now you can use them!
print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    # sql_command can be any select sql statement to get the data you need
    sql_command = "SELECT * FROM Movies WHERE Year >1985"
    cursor = conn.execute(sql_command)
    for row in cursor:
        print(f"The movie {row[1]} was released in {row[2]}")

print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies"
    cursor = conn.execute(sql_command)
    movies = cursor.fetchall()
    print(movies)
