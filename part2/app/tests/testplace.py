#!/usr/bin/python3
"""Testing place endpoint"""
import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUP(self):
        self.app = create_app()
        self.client = self.app.test_client()

        user_response = self.client.post('/api/v1/user/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com"
        })

        self.user_id = user_response.get_json()["id"]
    def test_create_place(self):
        response = self.client.post('/api/v1/place/', json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": self.user_id
            })
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_data(self):
        response = self.client.post('/api/v1/place/', json={
            "title": "",
            "description": "",
            "price": -1,
            "latitude": 190,
            "longitude": -190,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main(verbosity=2)
