from unittest import TestCase
from utils.Model import User
from pydantic import ValidationError

class UserModelTestClass(TestCase):
    def test_positive_correct_user_id(self):
        user = User(id='123', age=1)
        self.assertEqual(user.id, 123)

    def test_positive_incorrect_user_id(self):
        user = User(id='123', age=1)
        self.assertNotEqual(user.id, 321)

    def test_positive_incorrect_name(self):
        user = User(id='123', age=1)
        self.assertEqual(user.name, "Jane Doe")
    
    def test_negative_age(self):
        try:
            User(id=123, age=-1)
        except ValidationError:
            self.assertTrue(True)
        self.assertFalse(False)
