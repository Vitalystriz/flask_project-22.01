from flask import Flask, render_template
import sqlite3
app=Flask(__name__)

def get_db_connection():
    conn=sqlite3.connect("database.db")
    conn.row_factory=sqlite3.Row
    return conn


@app.route("/")
def draw_main_page():
    conn= get_db_connection()
    posts = conn.execute("SELECT * from posts").fetchall()
    conn.close()

    return render_template("index.html",posts=posts)
@app.route("/<int:post_id>")
def post(post_id):
    conn=get_db_connection()
    post= conn.execute("SELECT * from posts WHERE" )

@app.route("/about")
def description():





if __name__=="__main__":
    app.run()