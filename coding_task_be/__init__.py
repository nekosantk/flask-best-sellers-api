__version__ = "v0.0.1"

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.instance_path, 'data.db')
db = SQLAlchemy(app)


def create_app():
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():

        from . import routes

        create_db_tables()

        return app


def create_db_tables():
    with app.open_resource("schema.sql") as f:
        commands = f.read().decode("utf8").split(";")
        for command in commands:
            db.engine.execute(command)
