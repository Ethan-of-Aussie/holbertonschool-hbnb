from app.extensions import db
from sqlalchemy import ForeignKey, Column

place_amenity_association = db.Table(
    "place_amenity",
    Column("place_id", ForeignKey('places.id'), primary_key=True),
    Column("amenity_id", ForeignKey('amenities.id'), primary_key=True)
)