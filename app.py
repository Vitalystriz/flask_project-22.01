
from flask import Flask, render_template,request,flash,redirect,url_for
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///C:/Users/geras/PycharmProjects/flask_project-22.01/database1.db"
app.config["SECRET_KEY"] = "155555545456524"
from werkzeug.exceptions import abort
from forms import User_registration_form,User_log_in_form, add_Comment
# from alchemy_repositories import add_comment,get_all_comments,get_post
from repositories import *



@app.route("/")
def draw_main_page():
    posts=get_all_posts()
    return render_template("index.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/<int:post_id>')
def post(post_id):
    post_blog = get_post(post_id)
    post_comment = get_comments(post_id=post_id) #ЗАКОМЕНТИТЬ

    # user=get_users(user)
    if post_blog is None:
        abort(404)

    return render_template('post.html', post=post_blog, comments = post_comment)

@app.route('/<int:post_id>/comments/create',methods = ('GET','POST'))
def create_comment(post_id):
    form = add_Comment()
    if form.validate_on_submit():
        text = form.text.data
        print(text)
        add_comment(post_id=post_id,text=text)
        return redirect(url_for('post', post_id=post_id))

    return render_template('create_comment.html', form=form)


@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method=="POST":
        title=request.form["title"]
        content = request.form["content"]

        if not title:
            flash("Tittle is required")
        insert_into_posts(title,content)
        return redirect(url_for('draw_main_page'))

    return render_template("create.html")

@app.route("/<int:post_id>/edit", methods=("GET", "POST"))
def edit(post_id):
    if request.method=="POST":
        title=request.form["title"]
        content = request.form["content"]
        update_post(post_id=post_id,title=title,content=content)
        return redirect(url_for('draw_main_page'))

    return render_template("create.html")
@app.route("/<int:post_id>/delete",methods=("POST",))
def delete(post_id):
    delete_post(post_id=post_id)
    return redirect(url_for('draw_main_page'))


@app.route("/sign_in", methods=("GET", "POST"))
def sign_in():
    if request.method=="POST":
        name=request.form["name"]
        second_name = request.form["second_name"]

        if not name:
            flash("name  is required")
        # insert_into_users(name, second_name)
        return redirect(url_for('draw_main_page'))

    return render_template("sign_in.html")

@app.route('/register/', methods=["get", "post"])
def registration():
    form = User_registration_form()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password= form.password.data
        password_again= form. passwordRepeatFieled.data
        if password!=password_again:
            flash("Enter equal password")
        else:
            print(f'{name} {email}')

            add_user(name,email,password)

            return redirect(url_for("draw_main_page"))
    return render_template("registration.html", form=form)


#
# @app.route("/personal_cabinet")
# @login_required
# def personal_cabinet():
#     return render_template('personal.html')


if __name__=="__main__":
    app.run()