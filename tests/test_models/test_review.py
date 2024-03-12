#!/usr/bin/env python3

""" Unittest Cases for Review Model Class """

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review_creation(self):
        """Test Review creation with default values."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_review_with_arguments(self):
        """Test Review creation with specific values."""
        review = Review(place_id='123', user_id='456', text='Great experience!')
        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'Great experience!')

    def test_review_attribute_default(self):
        """Test Review attribute default value."""
        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_review_to_dict(self):
        """Test Review object serialization."""
        review_data = {
            'place_id': '789',
            'user_id': '101',
            'text': 'Nice place to stay'
        }
        review = Review(**review_data)
        review_dict = review.to_dict()
        self.assertEqual(review_dict['place_id'], review_data['place_id'])
        self.assertEqual(review_dict['user_id'], review_data['user_id'])
        self.assertEqual(review_dict['text'], review_data['text'])
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_review_str_representation(self):
        """Test string representation of Review object."""
        review = Review(place_id='789', user_id='101', text='Nice place to stay')
        expected_str = ("[Review] ({}) {{'place_id': '789', 'user_id': '101', 'text': 'Nice place to stay', 'id': '{}',"
                        "'created_at': '{}', 'updated_at': '{}'}}").format(review.id, review.created_at, review.updated_at)
        self.assertEqual(str(review), expected_str)


if __name__ == '__main__':
    unittest.main()
