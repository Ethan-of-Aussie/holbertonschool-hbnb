from app.models.base_model import BaseModel
from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(254), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    place_id = Column(Integer, ForeignKey('places.id'), nullable=False)
