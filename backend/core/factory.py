import os
from flask import Flask

from core.ext import db, ma, migrate
from core.utils.celery import init_celery
from apps.portal.api.routes import api_blueprint

def create_app(**kwargs) -> Flask:
    app = Flask(__name__)

    # initiate celery
    if kwargs.get("celery"):
        init_celery(app=app, celery=kwargs.get("celery"))

    # env params
    env = os.environ.get("FLASK_ENV")
    if env == "development":
        print("Run In Development Mode")
        app.config.from_object("core.config.DevelopmentConfig")
    else:
        print("Run In Production Mode")
        app.config.from_object("core.config.ProductionConfig")

    

    # initialize apps

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # register blueprint
    app.register_blueprint(api_blueprint)


    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app