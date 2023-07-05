#!/usr/bin/python3
"""We test te class Base Model and all its functions"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""
    def testBase(self):
        """A test to check if all values are the correct type"""
        B1 = BaseModel()
        self.assertIsInstance(B1.id, str)
        self.assertIsInstance(B1.created_at, datetime)
        self.assertIsInstance(B1.updated_at, datetime)

    def testSave(self):
        """a test to check if the save function changes the
        value of update_at"""
        B2 = BaseModel()
        prevUp = B2.updated_at
        B2.save()
        self.assertNotEquals(prevUp, B2.updated_at)

    def testToDict(self):
        """a test that check if to dict function work correctly"""
        B3 = BaseModel()
        keys = ['id', 'created_at', 'updated_at', '__class__']
        b3_dict = B3.to_dict()
        for key in keys:
            self.assertIn(key, b3_dict)


if __name__ == '__main__':
    unittest.main()
