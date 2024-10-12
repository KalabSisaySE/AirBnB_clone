#!/usr/bin/python3
"""loads all files stored in the storage(file.json)"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
