#!/usr/bin/python3
"""We test te class Base Model and all its functions"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSetUp(self):
        """Check if you can generate an instance"""
        self.B = BaseModel()

    def testExist(self):
        """A function that check if the base model attributes exists"""
        B5 = BaseModel()
        self.assertTrue(hasattr(B5, "id"))
        self.assertTrue(hasattr(B5, "created_at"))
        self.assertTrue(hasattr(B5, "updated_at"))

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

    def testTodictFormat(self):
        """a test for the isoformat values"""
        B4 = BaseModel()
        b4_dict = B4.to_dict()
        created_at = datetime.fromisoformat(b4_dict['created_at'])
        updated_at = datetime.fromisoformat(b4_dict['updated_at'])
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""unitest for base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_exist(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_type(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dictionary(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        obj_dict = self.model.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_has_correct_values(self):
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(obj_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str_representation(self):
        str_repr = str(self.model)
        self.assertIn(self.model.__class__.__name__, str_repr)
        self.assertIn(self.model.id, str_repr)
        self.assertIn(str(self.model.__dict__), str_repr)


if __name__ == '__main__':
    unittest.main()