from flask import Flask, render_template
from . import router

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    app.register_blueprint(router.bp)

    return app