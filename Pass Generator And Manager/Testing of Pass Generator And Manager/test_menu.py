import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pass_Generator_And_Manager import PasswordApp

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    @patch('builtins.input', side_effect=['1'])
    def test_menu_generate_password(self, mock_input):
        self.assertEqual(self.app.menu(), 1)

    @patch('builtins.input', side_effect=['2'])
    def test_menu_check_strength(self, mock_input):
        self.assertEqual(self.app.menu(), 2)

    @patch('builtins.input', side_effect=['3'])
    def test_menu_exit(self, mock_input):
        self.assertEqual(self.app.menu(), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)