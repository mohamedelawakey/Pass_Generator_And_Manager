import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
from Pass_Generator_And_Manager import PasswordApp

class TestPasswordLength(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    @patch('builtins.input', side_effect=[''])
    def test_password_length_default(self, mock_input):
        self.assertEqual(self.app.password_length(), 12)

    @patch('builtins.input', side_effect=['10'])
    def test_password_length_custom(self, mock_input):
        self.assertEqual(self.app.password_length(), 10)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)