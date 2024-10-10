#!/usr/bin/python3
"""test cases for the base class BaseModel"""
from datetime import datetime
import time
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test cases for the base class BaseModel"""

    def test_base_model_instantiation(self):
        """test the BaseModel instantiation"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertEqual(type(bm1.id), str)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_base_model_string_representation(self):
        """test the BaseModel's string representation"""
        bm = BaseModel()
        str_rep = str(bm)

        self.assertIn("[BaseModel]", str_rep)
        self.assertIn(bm.id, str_rep)
        self.assertIn(str(bm.__dict__), str_rep)

    def test_base_model_save(self):
        """test the `BaseModel` `save` method"""
        bm1 = BaseModel()
        old_updated_at = bm1.updated_at
        time.sleep(0.001)
        bm1.save()
        self.assertNotEqual(old_updated_at, bm1.updated_at)

    def test_base_model_to_dict(self):
        """test the `BaseModel` `to_dict` method"""
        bm1 = BaseModel()
        bm1.first_name = "Kalab"
        bm1.last_name = "Sisay"

        bm1_dict = bm1.to_dict()
        self.assertIn("first_name", bm1_dict)
        self.assertIn(bm1_dict["last_name"], "Sisay")
        self.assertEqual(type(bm1.first_name), str)

        self.assertIn("created_at", bm1_dict)
        self.assertIn("updated_at", bm1_dict)
        self.assertIsInstance(bm1_dict["created_at"], str)
        self.assertIsInstance(bm1_dict["updated_at"], str)
        self.assertIn("__class__", bm1_dict)
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
