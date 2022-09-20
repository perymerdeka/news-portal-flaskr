from core.ext import db

class PortalModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    link = db.Column(db.String())
    date = db.Column(db.String())
    images = db.Column(db.String())

    def __init__(self, title, link, date, images) -> None:
        self.title = title
        self.link = link
        self.date = date
        self.images = images

        def __repr__(self) -> str:
            return "".format(self.title)