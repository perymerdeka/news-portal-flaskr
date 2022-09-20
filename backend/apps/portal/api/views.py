import json
from flask_restx import Resource
from flask import jsonify, request

from modules.scraper import get_data
from apps.portal.api.schema import portal_schema, portals_schema
from apps.portal.models import PortalModel
from core.ext import db

class ScraperListView(Resource):
    url: str = "https://sport.detik.com/indeks"
    def get(self):
        scraper = PortalModel.query.all()
        return portals_schema.dump(scraper)
    
    def post(self):
       scraper = get_data(self.url)
       return jsonify(
        {
            "message": "Scraper Success"
        }
       )

class ScraperView(Resource):
    def get(self, news_id: int):
        scraper = PortalModel.query.get_or_404(news_id)
        return portal_schema.dump(scraper)
    
    def patch(self, news_id: int):
        news: PortalModel = PortalModel.query.get_or_404(news_id)

        if "link" or "title" or "date" or "images" in request.json:
            news.title = request.json["title"]
            news.date = request.json["date"]
            news.link = request.json["link"]
            news.images = request.json["images"]
        
        db.session.commit()
        return portal_schema.dump(news)

    def delete(self, scraper_id: int):
        scraper: PortalModel = PortalModel.query.get_or_404(scraper_id)
        db.session.delete(scraper)
        db.session.commit()
        return jsonify({"message": "Data deleted", "status": 204})
        

