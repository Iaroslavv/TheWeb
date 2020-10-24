from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import Post
from app.models import Comment


@app.route("/")
@app.route("/main")
def index():
    title = "Iaroslav Bulimov Music"
    return render_template("layout.html", title=title)


@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)


@app.route("/songs")
def songs():
    title = "Songs"
    return render_template("songs.html", title=title)


@app.route("/comments", methods=["POST", "GET"])
def comments():
    posts = Comment.query.order_by(Comment.date_posted.desc())
    return render_template("all_comments.html", posts=posts)


@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    form = Post()
    if form.validate_on_submit():
        post = Comment(comment=form.text.data)
        db.session.add(post)
        db.session.commit()
        flash("Thanks for your feedback!", "success")  # need to fix
        return redirect(url_for("comments"))
    return render_template(
        "feedback.html",
        form=form,
    )
