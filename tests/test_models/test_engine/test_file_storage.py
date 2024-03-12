#!/usr/bin/env python3

""" Unittests for file storage model class """

import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_new_object(self):
        class TestObj:
            def __init__(self, id, name):
                self.id = id
                self.name = name
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            def to_dict(self):
                return {
                    'id': self.id,
                    'name': self.name,
                    'created_at': self.created_at.isoformat(),
                    'updated_at': self.updated_at.isoformat()
                }

        obj1 = TestObj(1, "Object 1")
        self.storage.new(obj1)
        self.assertIn('TestObj.1', self.storage.all())

    def test_update_object(self):
        class TestObj:
            def __init__(self, id, name):
                self.id = id
                self.name = name
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            def to_dict(self):
                return {
                    'id': self.id,
                    'name': self.name,
                    'created_at': self.created_at.isoformat(),
                    'updated_at': self.updated_at.isoformat()
                }

        obj1 = TestObj(1, "Object 1")
        self.storage.new(obj1)

        obj1.name = "Updated Object 1"
        self.storage.new(obj1)
        self.assertEqual(self.storage.all()['TestObj.1'].name, "Updated Object 1")

    def test_save_reload(self):
        class TestObj:
            def __init__(self, id, name):
                self.id = id
                self.name = name
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            def to_dict(self):
                return {
                    'id': self.id,
                    'name': self.name,
                    'created_at': self.created_at.isoformat(),
                    'updated_at': self.updated_at.isoformat()
                }

        obj1 = TestObj(1, "Object 1")
        obj2 = TestObj(2, "Object 2")

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn('TestObj.1', new_storage.all())
        self.assertIn('TestObj.2', new_storage.all())


if __name__ == '__main__':
    unittest.main()
