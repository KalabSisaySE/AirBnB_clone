#!/usr/bin/python3
"""tests for state.py"""
import unittest

from models.state import State


class TestState(unittest.TestCase):
    """tests for the `State` model"""

    def test_state_instantiation(self):
        """tests for attributes of the `State` model"""
        state = State()

        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "name"))

        self.assertIsInstance(state.name, str)
