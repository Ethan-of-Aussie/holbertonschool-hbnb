from app.models.base_model import BaseModel
from app.extensions import db

class Place(BaseModel):
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(254), nullable = False)
    price = db.Column(db.Float, nullable = False)
    latitude = db.Column(db.Float, nullable = False)
    longitude = db.Column(db.Float, nullable = False)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)