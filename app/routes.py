from app import app
from flask import render_template


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
