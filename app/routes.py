from app import app


@app.route("/about")
def index():
    return "Hello world"
