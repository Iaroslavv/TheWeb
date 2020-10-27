from app import app, db, mail
from flask import (
    render_template,
    redirect, url_for,
    flash, current_app,
    request,
)
from app.forms import Post, Email
from app.models import Comment
from flask_mail import Message


@app.route("/main")
def main():
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


@app.route("/")
@app.route("/comments", methods=["POST", "GET"])
def comments():
    page = request.args.get("page", 1, type=int)
    posts = Comment.query.order_by(Comment.date_posted.desc()).paginate(
        page=page, per_page=5,
        )
    return render_template("all_comments.html", posts=posts)


@app.route("/support", methods=["POST", "GET"])
def support():
    pass


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


@app.route("/contact", methods=["POST", "GET"])
def contact():
    form = Email()
    if form.validate_on_submit():
        msg = Message(
                subject=form.title.data,
                body=form.text.data,
                sender=current_app.config["MAIL_USERNAME"],
                recipients=["yaroslaw.bulimov@yandex.ru"]
                )
        mail.send(msg)
        flash("Email was successfully sent!", "success")
        return redirect(url_for("main"))
    return render_template("contact.html", form=form)
