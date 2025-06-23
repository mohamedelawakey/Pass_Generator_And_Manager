import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pass_Generator_And_Manager import PasswordApp

class TestGetNumPass(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    @patch('builtins.input', side_effect=[''])
    def test_get_num_pass_default(self, mock_input):
        self.assertEqual(self.app.get_num_pass(), 1)

    @patch('builtins.input', side_effect=['2'])
    def test_get_num_pass_custom(self, mock_input):
        self.assertEqual(self.app.get_num_pass(), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)