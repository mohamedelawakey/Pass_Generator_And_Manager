import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import string
from Pass_Generator_And_Manager import PasswordApp

class TestGeneratePass(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    def test_generate_pass_length_and_content(self):
        password = self.app.generate_pass(12)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)