import os

from flask import Flask


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'tradehub.sqlite')
    )

    if test_config is None:
        # Load the instance of config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_pyfile(test_config)

    # Ensure the instance folder exists
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    from . import home
    app.register_blueprint(home.bp)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
