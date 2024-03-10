import unittest
from datetime import datetime
from unittest.mock import MagicMock
from models.base_model import BaseModel  # Import your BaseModel class


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        # Test regular initialization
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

        # Test initialization from kwargs
        data = {
            'id': '1234',
            'created_at': '2024-03-10T12:00:00.000',
            'updated_at': '2024-03-10T13:00:00.000'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.created_at, datetime(2024, 3, 10, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2024, 3, 10, 13, 0, 0))

    def test_save(self):
        storage_mock = MagicMock()
        BaseModel.set_storage(storage_mock)
        model = BaseModel()
        model.save()
        self.assertIsNotNone(model.updated_at)
        storage_mock.save.assert_called_once()

        # Test new instance addition to storage
        model.id = None
        model.save()
        storage_mock.new.assert_called_once_with(model)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)


if __name__ == '__main__':
    unittest.main()
