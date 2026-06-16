#!/usr/bin/python3


from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User related methods
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_users(self, user_id, user_data):
        return self.user_repo.update(user_id, user_data)

    # Amenities related methods
    def create_amenity(self, amenity_date):
        amenity = Amenity(**amenity_date)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder
        amenities = self.amenity_repo.get_all()
        return [dict.__dict__ for dict in amenities]

    def update_amenity(self, amenity_id, amenity_data):
        # Not sure if done
        return self.amenity_repo.update(amenity_id, amenity_data)

    # Place realted methods
    def create_place(self, place_data):
        if not isinstance(place_data["price"], float):
            raise TypeError("price data need to be of type float")
        if place_data["price"] < 0:
            raise ValueError("price need to be positive number")
        if place_data["latitude"] < -90 or place_data["latitude"] > 90:
            raise ValueError("latitude must be between -90 and 90")
        if place_data["longitude"] < -180 or place_data["longitude"] > 180:
            raise ValueError("longitude must be between -180 and 180")

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        # Placeholder
        pass

    # Review realated methods
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Placeholder
        pass

    def update_review(self, review_id, review_data):
        return self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        # Placeholder
        pass
