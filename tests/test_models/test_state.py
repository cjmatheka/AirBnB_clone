#!/usr/bin/env python3

""" Unittest Cases for State Model Class """

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_creation(self):
        """Test State creation with default values."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, '')

    def test_state_with_arguments(self):
        """Test State creation with specific values."""
        state = State(name='California')
        self.assertEqual(state.name, 'California')

    def test_state_attribute_default(self):
        """Test State attribute default value."""
        state = State()
        self.assertEqual(state.name, '')

    def test_state_to_dict(self):
        """Test State object serialization."""
        state_data = {
            'name': 'New York',
        }
        state = State(**state_data)
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], state_data['name'])
        self.assertEqual(state_dict['__class__'], 'State')

    def test_state_str_representation(self):
        """Test string representation of State object."""
        state = State(name='Texas')

        expected_str = (
            f"[State] ({state.id}) {{'name': 'Texas', 'id': '{state.id}', "
            f"'created_at': '{state.created_at}', 'updated_at': '{state.updated_at}'}}"
        )

        self.assertEqual(str(state), expected_str)


if __name__ == '__main__':
    unittest.main()
