from app.models.base_model import BaseModel
from app.extensions import db

class Review(BaseModel):
    text = db.Column(db.String(254), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
