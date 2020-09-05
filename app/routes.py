from app import app
from flask import render_template


@app.route("/about")
def index():
    mytitle = "Heyheyehey"
    return render_template("layout.html", mytitle=mytitle)
