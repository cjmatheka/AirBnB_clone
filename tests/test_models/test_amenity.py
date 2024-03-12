#!/usr/bin/python3

""" Unittests for Amenity Model Class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        """Test Amenity creation with default values."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, '')

    def test_amenity_with_arguments(self):
        """Test Amenity creation with specific values."""
        amenity = Amenity(name='WiFi')
        self.assertEqual(amenity.name, 'WiFi')

    def test_amenity_attribute_default(self):
        """Test Amenity attribute default value."""
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_amenity_to_dict(self):
        """Test Amenity object serialization."""
        amenity_data = {
            'name': 'Pool',
        }
        amenity = Amenity(**amenity_data)
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], amenity_data['name'])
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_str_representation(self):
        """Test string representation of Amenity object."""
        amenity = Amenity(name='Gym')
        expected_str = ("[Amenity] ({}) {'name': 'Gym', 'id': '{}', 'created_at': '{}',"
                        "'updated_at': '{}'}").format(amenity.id, amenity.created_at, amenity.updated_at)
        self.assertEqual(str(amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
