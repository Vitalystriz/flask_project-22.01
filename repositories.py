import sqlite3

def get_db_connection():
    conn=sqlite3.connect("C:/Users/geras/PycharmProjects/flask_project-22.01/database.db")
    conn.row_factory=sqlite3.Row
    return conn
def add_user(name,email,password):
    conn=get_db_connection()
    conn.execute("INSERT INTO users(name, email, password) VALUES (?,?,?)",(name,email,password))
    conn.commit()
    conn.close()
def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute("SELECT * from posts").fetchall()
    conn.close()
    return posts

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post
def get_users(user):
    conn2 = get_db_connection()
    user = conn2.execute('SELECT * FROM users WHERE second_name = ?',
                        (user,)).fetchone()
    conn2.close()
    return user
def insert_into_posts(title,content):
    conn = get_db_connection()
    conn.execute("INSERT INTO posts (title,content) VALUES(?,?)", (title, content))
    conn.commit()
    conn.close()
# def insert_into_users(name, second_name):
#     conn = get_db_connection()
#     conn.execute("INSERT INTO users (name,second_name) VALUES(?,?)", (name, second_name))
#     conn.commit()
#     conn.close()