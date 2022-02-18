import sqlite3

connection=sqlite3.connect("C:/Users/geras/PycharmProjects/flask_project-22.01/database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cursor=connection.cursor()
cursor.execute("INSERT INTO posts (title,content) VALUES(?,?)",("Пост1 "," Контент"))
cursor=connection.cursor()
cursor.execute("INSERT INTO posts (title,content) VALUES(?,?)",("Пост2 "," Контент2"))


connection.commit()
connection.close()