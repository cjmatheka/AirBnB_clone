#!/usr/bin/env python3

"""
Test cases for base_model
Test Cases:
    instantiation
    save
    to_dict
"""

import os
from models import storage
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Test cases for proper instantiation of the BaseModel class."""

    def test_instantiation_without_arguments(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids_for_two_models(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_different_created_at_for_two_models(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_different_updated_at_for_two_models(self):
        model1 = BaseModel()
        sleep(0.08)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_string_representation(self):
        dtm = datetime.today()
        dtm_repr = repr(dtm)
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = dtm
        model_str = model.__str__()
        self.assertIn("[BaseModel] (123456)", model_str)
        self.assertIn("'id': '123456'", model_str)
        self.assertIn("'created_at': " + dtm_repr, model_str)
        self.assertIn("'updated_at': " + dtm_repr, model_str)

    def test_unused_arguments(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_instantiation_with_keyword_arguments(self):
        dtm = datetime.today()
        dtm_iso = dtm.isoformat()
        model = BaseModel(id="345", created_at=dtm_iso, updated_at=dtm_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, dtm)
        self.assertEqual(model.updated_at, dtm)

    def test_instantiation_without_keyword_arguments(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_arguments_and_keyword_arguments(self):
        dtm = datetime.today()
        dtm_iso = dtm.isoformat()
        model = BaseModel("12", id="345",
                          created_at=dtm_iso, updated_at=dtm_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, dtm)
        self.assertEqual(model.updated_at, dtm)


class TestBaseModelSave(unittest.TestCase):
    """Test Cases for base model save method."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def test_one_save_updates_time(self):
        model = BaseModel()
        sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_two_saves_update_time_correctly(self):
        model = BaseModel()
        sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        second_updated_at = model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        model.save()
        self.assertLess(second_updated_at, model.updated_at)

    def test_save_with_argument_raises_exception(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save()

    def test_save_updates_file_content(self):
        model = BaseModel()
        model.save()
        model_key = "BaseModel." + model.id
        with open("file.json", "r") as f:
            self.assertIn(model_key, f.read())


class TestBaseModelToDict(unittest.TestCase):
    """Unit tests for testing to_dict method of the BaseModel class."""

    def test_to_dict_returns_dictionary(self):
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        model = BaseModel()
        keys = model.to_dict().keys()
        self.assertSetEqual(set(keys),
                            {"id", "created_at",
                             "updated_at", "__class__"})

    def test_to_dict_contains_added_attributes(self):
        model = BaseModel()
        model.name = "Sweet"
        model.my_number = 147
        dict_keys = model.to_dict().keys()
        self.assertIn("name", dict_keys)
        self.assertIn("my_number", dict_keys)

    def test_to_dict_datetime_attributes_are_strings(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_to_dict_output(self):
        dtm = datetime.today()
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = dtm
        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dtm.isoformat(),
            'updated_at': dtm.isoformat()
        }
        self.assertDictEqual(model.to_dict(), expected_dict)

    def test_to_dict_is_different_from_dunder_dict(self):
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_to_dict_with_argument_raises_exception(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict()


if __name__ == "__main__":
    unittest.main()
