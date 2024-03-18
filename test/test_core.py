import pytest
from unittest.mock import patch
from core import show_menu

# Example test for the show_menu function
def test_show_menu():
  with patch('builtins.input', return_value='1'), patch('builtins.print') as mock_print:
    choice = show_menu("main")
    mock_print.assert_called_with("1) KAD/ADC/109/C/S1/03")
    assert choice == '1'
