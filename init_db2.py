import sqlite3

connection=sqlite3.connect("database2.db")

with open("schema2.sql") as f:
    connection.executescript(f.read())

cursor=connection.cursor()
cursor.execute("INSERT INTO users (title,content) VALUES(?,?)",("Виталий "," Стрижевский"))


connection.commit()
connection.close()