#!/usr/bin/env python3

""" Unittests for City Model Class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_city_creation(self):
        """Test City creation with default values."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_city_with_arguments(self):
        """Test City creation with specific values."""
        city = City(state_id='NY', name='New York')
        self.assertEqual(city.state_id, 'NY')
        self.assertEqual(city.name, 'New York')

    def test_city_attribute_default(self):
        """Test City attribute default value."""
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_city_to_dict(self):
        """Test City object serialization."""
        city_data = {
            'state_id': 'CA',
            'name': 'Los Angeles',
        }
        city = City(**city_data)
        city_dict = city.to_dict()
        self.assertEqual(city_dict['state_id'], city_data['state_id'])
        self.assertEqual(city_dict['name'], city_data['name'])
        self.assertEqual(city_dict['__class__'], 'City')

    def test_city_str_representation(self):
        """Test string representation of City object."""
        city = City(state_id='CA', name='Los Angeles')
        expected_str = ("[City] ({}) {{'state_id': 'CA', 'name': 'Los Angeles', 'id': '{}',"
                        "'created_at': '{}', 'updated_at': '{}'}}").format(city.id, city.created_at, city.updated_at)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
