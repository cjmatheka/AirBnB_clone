#!/usr/bin/python3

""" Unittest Cases for Place Model Class """

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        """Test Place creation with default values."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_with_arguments(self):
        """Test Place creation with specific values."""
        place = Place(city_id='NY', user_id='1', name='Cozy Apartment', description='Nice place', number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100, latitude=40.7128, longitude=-74.0060, amenity_ids=[1, 2, 3])
        self.assertEqual(place.city_id, 'NY')
        self.assertEqual(place.user_id, '1')
        self.assertEqual(place.name, 'Cozy Apartment')
        self.assertEqual(place.description, 'Nice place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

    def test_place_attribute_default(self):
        """Test Place attribute default value."""
        place = Place()
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_to_dict(self):
        """Test Place object serialization."""
        place_data = {
            'city_id': 'CA',
            'user_id': '2',
            'name': 'Beach House',
            'description': 'Beautiful house by the beach',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 200,
            'latitude': 34.0522,
            'longitude': -118.2437,
            'amenity_ids': [4, 5, 6]
        }
        place = Place(**place_data)
        place_dict = place.to_dict()
        self.assertEqual(place_dict['city_id'], place_data['city_id'])
        self.assertEqual(place_dict['user_id'], place_data['user_id'])
        self.assertEqual(place_dict['name'], place_data['name'])
        self.assertEqual(place_dict['description'], place_data['description'])
        self.assertEqual(place_dict['number_rooms'], place_data['number_rooms'])
        self.assertEqual(place_dict['number_bathrooms'], place_data['number_bathrooms'])
        self.assertEqual(place_dict['max_guest'], place_data['max_guest'])
        self.assertEqual(place_dict['price_by_night'], place_data['price_by_night'])
        self.assertEqual(place_dict['latitude'], place_data['latitude'])
        self.assertEqual(place_dict['longitude'], place_data['longitude'])
        self.assertEqual(place_dict['amenity_ids'], place_data['amenity_ids'])
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_place_str_representation(self):
        """Test string representation of Place object."""
        place = Place(city_id='CA', user_id='2', name='Beach House', description='Beautiful house by the beach',
                      number_rooms=3, number_bathrooms=2, max_guest=6, price_by_night=200, latitude=34.0522, longitude=-118.2437, amenity_ids=[4, 5, 6])
        expected_str = ("[Place] ({}) {{'city_id': 'CA', 'user_id': '2', 'name': 'Beach House',"
                        "'description': 'Beautiful house by the beach', 'number_rooms': 3, 'number_bathrooms': 2,"
                        "'max_guest': 6, 'price_by_night': 200, 'latitude': 34.0522, 'longitude': -118.2437,"
                        "'amenity_ids': [4, 5, 6], 'id': '{}', 'created_at': '{}', 'updated_at': '{}'}}").format(place.id, place.created_at, place.updated_at)
        self.assertEqual(str(place), expected_str)


if __name__ == '__main__':
    unittest.main()
