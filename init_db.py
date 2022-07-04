import sqlite3

connection=sqlite3.connect("C:/Users/geras/PycharmProjects/flask_project-22.01/database1.db")

# with open("schema.sql") as f:
#     connection.executescript(f.read())

cursor=connection.cursor()
# cursor.execute("INSERT INTO posts (title,content) VALUES(?,?)",("Пост1 "," Контент"))
# cursor=connection.cursor()
# cursor.execute("INSERT INTO posts (title,content) VALUES(?,?)",("Пост2 "," Контент2"))
# cursor=connection.cursor()
# cursor.execute("INSERT INTO comments (post_id,content) VALUES(?,?)",(1," Комент"))

for row in cursor.execute("SELECT * FROM users"):
    print(row)

# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())
connection.commit()
connection.close()