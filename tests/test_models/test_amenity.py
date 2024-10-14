#!/usr/bin/python3
"""tests for amenity.py"""
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests for the `Amenity` model"""

    def test_amenity_instantiation(self):
        """tests for attributes of the `Amenity` model"""
        amenity = Amenity()

        self.assertTrue(hasattr(amenity, "name"))

        self.assertIsInstance(amenity.name, str)
