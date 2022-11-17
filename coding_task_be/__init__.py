import os
from flask import Flask


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'data.db'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():

        from . import routes

        from . import db
        db.init_app(app)

        return app
