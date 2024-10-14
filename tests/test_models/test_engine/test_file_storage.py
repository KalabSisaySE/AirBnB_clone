#!/usr/bin/python3
"""tests for file_storage.py"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """tests for file_storage.py"""

    @classmethod
    def setUpClass(cls):
        """declares variables for the entire test class"""
        cls.objects = FileStorage._FileStorage__objects
        cls.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """removes stored data in file"""
        file_path = self.__class__.file_path
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_file_storage_objects(self):
        """test file storage's object adding"""
        bm = BaseModel()
        self.assertIn(f"BaseModel.{bm.id}", self.__class__.objects)
        if os.path.exists(self.__class__.file_path):
            with open(self.__class__.file_path, "r") as file:
                data = json.load(file)
                self.assertNotIn(f"BaseModel.{bm.id}", data)

        bm.save()

        self.assertTrue(os.path.exists(self.__class__.file_path))
        with open(self.__class__.file_path, "r") as file:
            data = json.load(file)
            self.assertIn(f"BaseModel.{bm.id}", data)
            self.assertEqual(data[f"BaseModel.{bm.id}"], bm.to_dict())

    def test_file_storage_models(self):
        """test file storage's model handling"""
        user = User()
        self.assertTrue(self.__class__.objects.get(f"User.{user.id}"))
        user.save()
        with open(self.__class__.file_path, "r") as file:
            data = json.load(file)
            self.assertIn(f"User.{user.id}", data)
            self.assertEqual(data[f"User.{user.id}"], user.to_dict())
