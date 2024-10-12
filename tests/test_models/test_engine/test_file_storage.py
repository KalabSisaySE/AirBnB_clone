#!/usr/bin/python3
"""tests for file_storage.py"""
import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        bm.save()

        self.assertTrue(os.path.exists(self.__class__.file_path))
        with open(self.__class__.file_path, "r") as file:
            data = json.load(file)
            self.assertIn(f"BaseModel.{bm.id}", data)
            self.assertEqual(data[f"BaseModel.{bm.id}"], bm.to_dict())
