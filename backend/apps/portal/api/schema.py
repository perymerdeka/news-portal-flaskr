from core.ext import ma
from apps.portal.models import PortalModel


class PortalScraperSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PortalModel
        include_fk = True

# schema
portal_schema: PortalScraperSchema = PortalScraperSchema()
portals_schema: PortalScraperSchema = PortalScraperSchema(many=True)