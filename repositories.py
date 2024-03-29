import sqlite3

def get_db_connection():
    conn=sqlite3.connect("C:/Users/geras/PycharmProjects/flask_project-22.01/database1.db")
    conn.row_factory=sqlite3.Row
    # conn.execute("DELETE  FROM users ")
    # conn.commit()

    cursor = conn.cursor()
    result = cursor.execute('SELECT * FROM users')
    rows = result.fetchall()
    for row in rows:
        # print(row[0]+row[1]+row[2]+row[3]+row[4]+row[5])
        # print(row['Name'])
        # print(row['name'])

        print(row[3])
    print("end")

    return conn
def add_user(name,login,email,password):
    conn=get_db_connection()
    conn.execute("INSERT INTO users(name,login, email, password_hash) VALUES (?,?,?,?)",(name,login,email,password))
    conn.commit()
    conn.close()
def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute("SELECT * from posts").fetchall()
    conn.close()
    return posts

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE post_id = ?',
                        (post_id,)).fetchone()
    conn.close()
    return post
def get_comments(post_id):
    conn = get_db_connection()
    comment = conn.execute('SELECT content FROM comments WHERE post_id = ?',
                        (post_id,)).fetchone()

    comments = conn.execute('SELECT * FROM comments WHERE post_id = ?',
                        (post_id,)).fetchall()
    print(comments)
    conn.close()

    return comments

def insert_into_posts(title,content):
    conn = get_db_connection()
    conn.execute("INSERT INTO posts (title,content) VALUES(?,?)", (title, content))
    conn.commit()
    conn.close()
def login_by_name(user_id):
    conn3 = get_db_connection()
    login = conn3.execute('SELECT login FROM users WHERE id = ?',
                            (user_id,)).fetchone()
    conn3.close()
    return login
def add_comment(post_id,text):
    conn = get_db_connection()
    print(post_id,text)
    conn.execute("INSERT INTO comments (post_id,content) VALUES(?,?)", (post_id, text))
    conn.commit()
    print(conn.execute('SELECT content FROM comments WHERE post_id = ?',
                        (post_id,)).fetchone())
    conn.close()
def delete_post(post_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM posts WHERE post_id=?",(post_id,))
    conn.commit()
    conn.close
def update_post(post_id,title,content):
    conn = get_db_connection()
    conn.execute("UPDATE posts SET title=? WHERE post_id=?",(title,post_id))
    conn.execute("UPDATE posts SET content=? WHERE post_id=?", (content,post_id))
    conn.commit()
    conn.close
def get_user_hash(name):

    conn = get_db_connection()
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM users WHERE name=?",(name,)).fetchone() #fetchone
    res = cursor.execute("SELECT * FROM users WHERE name=?",(name,)).fetchall()
    password = conn.execute("SELECT password_hash FROM users WHERE name=? ",(name,)).fetchone()


    rows = result[3]
    # password_hash = conn.execute("SELECT * FROM users WHERE name=?",(name,)).fetchall()
    print(res)
    print("pas")

    conn.close()
    return rows



# def insert_into_users(name, second_name):
#     conn = get_db_connection()
#     conn.execute("INSERT INTO users (name,second_name) VALUES(?,?)", (name, second_name))
#     conn.commit()
#     conn.close()
