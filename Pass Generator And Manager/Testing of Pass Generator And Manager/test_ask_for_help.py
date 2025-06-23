import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pass_Generator_And_Manager import PasswordApp

class TestAskForHelp(unittest.TestCase):
    def setUp(self):
        self.app = PasswordApp()

    @patch('builtins.input', return_value='n')
    @patch('sys.stdout', new_callable=StringIO)
    def test_ask_for_help_decline(self, mock_stdout, mock_input):
        self.app.ask_for_help()
        self.assertIn("no problem", mock_stdout.getvalue())
        
if __name__ == '__main__':
    unittest.main(verbosity=2)