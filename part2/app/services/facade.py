#!/usr/bin/python3


from app.persistence.repository import InMemoryRepository
from app.models.user import User

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
        return self.user_repo.get_all

    def update_users(self, user_id, user_data):
        pass

    # Amenities related methods
    def create_amenity(self, amenity_date):
        # Placeholder
        pass

    def get_amenity(self, amenity_id):
        # Placeholder
        pass

    def get_all_amenities(self):
        # Placeholder
        pass

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder
        pass

    # Place realted methods
    def create_place(self, place_data):
        # Placeholder
        pass

    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def get_all_places(self):
        # Placeholder
        pass

    def update_place(self, place_id, place_data):
        # Placeholder
        pass

    # Review realated methods
    def create_review(self, review_data):
        # Placeholder
        pass

    def get_review(self, review_id):
        # Placeholder
        pass

    def get_all_reviews(self):
        # Placeholder
        pass

    def get_reviews_by_place(self, place_id):
        # Placeholder
        pass

    def update_review(self, review_id, review_data):
        # Placeholder
        pass

    def delete_review(self, review_id):
        # Placeholder
        pass
