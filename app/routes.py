from app import app
from flask import render_template


@app.route("/")
def index():
    mytitle = "Heyheyehey"
    return render_template("layout.html", mytitle=mytitle)
