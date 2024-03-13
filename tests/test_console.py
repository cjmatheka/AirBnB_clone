#!/usr/bin/env python3

"""
Unitest cases for console
    Test_prompting
    TestH_help
    Test_exit
    Test_create
    Test_show
    Test_all
    Test_destroy
    Test_update
"""

from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_prompting(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.cmdloop()
            output = fake_out.getvalue().strip()
            self.assertTrue(output.startswith("(hbnb)"))

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_help(None)
            output = fake_out.getvalue().strip()
            self.assertTrue("Documented commands" in output)

    def test_exit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.do_quit(None))

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("User")
            output = fake_out.getvalue().strip()
            self.assertTrue(output.startswith("d-"))

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show("User 12345")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all("User")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy("User 12345")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update("User 12345 name John")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_EOF(self):
        h = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
