#!/usr/bin/python3
"""tests for user.py"""
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """tests for the `User` model"""

    def test_user_instantiation(self):
        """tests for attributes of the `User` model"""
        user = User()

        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.last_name, str)
