import sqlite3

connection=sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cursor=connection.cursor()
cursor.execute("INSERT INTO posts (title,content,description) VALUES(?,?,?)",("Пост1 "," Контент","Описание1"))
cursor=connection.cursor()
cursor.execute("INSERT INTO posts (title,content,description) VALUES(?,?,?)",("Пост2 "," Контент2","Описание2"))

connection.commit()
connection.close()