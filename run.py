from app import app

app.config.from_object("app.config.config")


if __name__ == "__main__":
    app.run()
