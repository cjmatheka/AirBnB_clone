#!/usr/bin/python3

""" Test cases for User Model """

import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        """Test user creation with default values."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_user_with_arguments(self):
        """Test user creation with specific values."""
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_user_attribute_defaults(self):
        """Test user attribute defaults."""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_user_to_dict(self):
        """Test user object serialization."""
        user_data = {
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_data)
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], user_data['email'])
        self.assertEqual(user_dict['password'], user_data['password'])
        self.assertEqual(user_dict['first_name'], user_data['first_name'])
        self.assertEqual(user_dict['last_name'], user_data['last_name'])
        self.assertEqual(user_dict['__class__'], 'User')

    def test_user_str_representation(self):
        """Test string representation of user object."""
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        expected_str = ("[User] ({}) {'email': 'test@example.com', 'password': 'password', 'first_name': 'John',"
                        "'last_name': 'Doe', 'id': '{}', 'created_at': '{}',"
                        "'updated_at': '{}'}").format(user.id, user.created_at, user.updated_at)
        self.assertEqual(str(user), expected_str)


if __name__ == '__main__':
    unittest.main()
