#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('builtins.input', side_effect=["create BaseModel"]):
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn("created", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        with patch('builtins.input', side_effect=["show BaseModel 1234"]):
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertIn("no instance found", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        with patch('builtins.input', side_effect=["destroy BaseModel 1234"]):
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertIn("no instance found", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        with patch('builtins.input', side_effect=["all BaseModel"]):
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("no instance found", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        with patch('builtins.input', side_effect=["update BaseModel 1234"]):
            HBNBCommand().onecmd("update BaseModel 1234")
            self.assertIn("no instance found", mock_stdout.getvalue())

    def test_quit(self):
        with patch('builtins.input', side_effect=["quit"]):
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch('builtins.input', side_effect=["EOF"]):
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
