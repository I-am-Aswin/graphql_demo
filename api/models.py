from datetime import date
from . import db

class Post( db.Model ):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(500))
    created_at = db.Column(db.Date, default=date.today().strftime("%d-%m-%y"))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime("%d-%m-%y"))
        }