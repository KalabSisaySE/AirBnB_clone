#!/usr/bin/python3
"""tests for review.py"""
import unittest

from models.review import Review


class TestReview(unittest.TestCase):
    """tests for the `Review` model"""

    def test_review_instantiation(self):
        """tests for attributes of the `Review` model"""
        review = Review()

        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
