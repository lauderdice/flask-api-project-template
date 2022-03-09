from typing import Tuple

import flask
from flask.app import Flask
from flask_pydantic_spec import FlaskPydanticSpec


from app.common.config import setup_flask_logging, setup_environment
import os

def create_application() -> flask.app.Flask:
    from app.api.healthcheck.routers import healthchecks
    from app.api.sample.routers import sample
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    setup_environment(os.path.join(os.path.dirname(os.path.abspath(__file__)), "common/env_files/.common_env"))
    app = setup_flask_logging(app)
    app.register_blueprint(healthchecks)
    app.register_blueprint(sample)
    return app

application = create_application()
