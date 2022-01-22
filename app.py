from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3
from werkzeug.exceptions import abort
app=Flask(__name__)

def get_db_connection():
    conn=sqlite3.connect("database.db")
    conn.row_factory=sqlite3.Row
    return conn

def get_db_connection2():
    conn=sqlite3.connect("database2.db")
    conn.row_factory=sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
@app.route("/")
def draw_main_page():
    conn= get_db_connection()
    posts = conn.execute("SELECT * from posts").fetchall()
    conn.close()

    return render_template("index.html",posts=posts)
# @app.route("/<int:post_id>")
# def post(post_id):
#     conn=get_db_connection()
#     post= conn.execute("SELECT * from posts". )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method=="POST":
        tittle=request.form["title"]
        content = request.form["content"]

        if not tittle:
            flash("Tittle is required")
        conn= get_db_connection()
        conn.execute("INSERT INTO posts (title,content) VALUES(?,?)", (tittle, content))
        conn.commit()
        conn.close()
        return redirect(url_for('draw_main_page'))

    return render_template("create.html")
@app.route("/sign_in", methods=("GET", "POST"))
def sign_in():
    if request.method=="POST":
        name=request.form["name"]
        second_name = request.form["second_name"]

        if not name:
            flash("Tittle is required")
        conn= get_db_connection()
        conn.execute("INSERT INTO users (name,second_name) VALUES(?,?)", (name, second_name))
        conn.commit()
        conn.close()
        return redirect(url_for('draw_main_page'))

    return render_template("create.html")
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
if __name__=="__main__":
    app.run()