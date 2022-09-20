from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

ma: Marshmallow = Marshmallow()
db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
