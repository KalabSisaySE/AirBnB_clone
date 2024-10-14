#!/usr/bin/python3
"""tests for city.py"""
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """tests for the `City` model"""

    def test_city_instantiation(self):
        """tests for attributes of the `City` model"""
        city = City()

        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
