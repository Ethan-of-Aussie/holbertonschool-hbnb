#!/usr/bin/python3
"""Testing place endpoint"""
import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUP(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        response = self.client.post('/api/v1/place/', json={
            })
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_data(self):
        response = self.client.post('/api/v1/place/', json={
            })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main(verbosity=2)
