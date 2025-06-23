import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from Pass_Generator_And_Manager import PasswordApp

class TestPasswordChecks(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    def test_has_upper(self):
        self.assertTrue(self.app.has_upper("A"))
        self.assertFalse(self.app.has_upper("a"))

    def test_has_lower(self):
        self.assertTrue(self.app.has_lower("a"))
        self.assertFalse(self.app.has_lower("A"))

    def test_has_number(self):
        self.assertTrue(self.app.has_number("1"))
        self.assertFalse(self.app.has_number("a"))

    def test_has_symbol(self):
        self.assertTrue(self.app.has_symbol("@"))
        self.assertFalse(self.app.has_symbol("a"))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)