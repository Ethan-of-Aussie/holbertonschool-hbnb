#!/usr/bin/python3
"""Testing review endpoint"""
import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        response = self.client.post('api/v1/reviews/', json={
            })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main(verbosity=2)
