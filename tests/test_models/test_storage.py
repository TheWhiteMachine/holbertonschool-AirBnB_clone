#!/usr/bin/python3
"""We test te class Base Model and all its functions"""
import unittest
from models.base_model import BaseModel
from models import storage


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def test_all(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.new(my_model)
        storage.save()
        Objects = storage.all()
        self.assertIsNotNone(Objects)

    def test_save_new(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.new(my_model)
        storage.save()

    def test_reload(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        storage.new(my_model)
        storage.save()
        objects = storage.reload()
        self.assertIsNotNone(objects)
