import sys
sys.path.append('path/to/your/module')
from unittest.mock import patch

from unit.core import show_menu


def test_show_menu_main():
  # Mock input to return '1' and capture print statements
  with patch('builtins.input', return_value='1'), patch('builtins.print') as mocked_print:
    assert show_menu("main") == '1'
    # Ensure that the expected call matches the actual call exactly, including whitespace
    mocked_print.assert_any_call('\nWelcome to the Debug Helper. Please choose the module as fallow ')
    # If you want to ignore whitespace differences, use .strip() on both strings
    # or adjust the string you're asserting against to include the newline if that's the intended behavior.
