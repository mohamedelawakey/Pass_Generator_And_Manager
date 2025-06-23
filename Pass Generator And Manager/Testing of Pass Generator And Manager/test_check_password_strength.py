import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pass_Generator_And_Manager import PasswordApp

class TestCheckPasswordStrength(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    @patch('builtins.input', return_value='Abcd1234!')
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_password_strength_very_strong(self, mock_stdout, mock_input):
        self.app.check_password_strength()
        self.assertIn("Very Strong", mock_stdout.getvalue())

    @patch('builtins.input', return_value='Abcd1234')
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_password_strength_strong(self, mock_stdout, mock_input):
        self.app.check_password_strength()
        self.assertIn("Strong", mock_stdout.getvalue())

    @patch('builtins.input', return_value='abcd1234')
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_password_strength_weak(self, mock_stdout, mock_input):
        self.app.check_password_strength()
        self.assertIn("make your password stronger", mock_stdout.getvalue())
        
    @patch('builtins.input', side_effect=['abcd1234', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_check_password_strength_weak(self, mock_stdout, mock_input):
        self.app.check_password_strength()
        output = mock_stdout.getvalue()
        self.assertIn("Okay, no problem", output)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    