from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config.config")
Bootstrap(app)
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
app.static_folder = 'static'
app.template_folder = 'templates'


from app import routes, models
