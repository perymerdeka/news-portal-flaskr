from flask import Blueprint
from flask_restx import Api

from apps.portal.api.views import *


api_blueprint: Blueprint = Blueprint("api", __name__)

api: Api = Api(
    api_blueprint,
    title="Portal Berita API",
    description="Portal Berita API",
    version="1.0",
    doc="/docs/",
    default="Portal Berita API",
    default_label="News API",
    default_mediatype="application/json",
)

api.add_resource(ScraperListView, "/news", endpoint="news")
api.add_resource(ScraperView, "/news/<int:news_id>", endpoint="")
