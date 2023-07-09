#!/usr/bin/python3
"""We test te class FileStorage and all its functions"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSetUp(self):
        """Check if you can generate an instance"""
        self.f = FileStorage()

    def test_all(self):
        """check if the all function returns some value after I add an
        object to json file"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.new(my_model)
        storage.save()
        Objects = storage.all()
        self.assertIsNotNone(Objects)
    

    def test_save_new(self):
        """Test if I can use the save function without problems"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.new(my_model)
        storage.save()

    def test_reload(self):
        """test if the reload returns an object"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.new(my_model)
        storage.save()
        objects = storage.reload()

