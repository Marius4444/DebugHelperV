# tests/test_core.py
# test_core.py

from unittest.mock import patch

from core import show_menu


def test_show_menu_main():
  # Mock input to return '1' and capture print statements
  with patch('builtins.input', return_value='1'), patch('builtins.print') as mocked_print:
    assert show_menu("main") == '1'
    # Check if the welcome prompt is printed
    mocked_print.assert_any_call("Welcome to the Debug Helper. Please choose the module as follow ")
    # Check if an option is printed
    mocked_print.assert_any_call("1) KAD/ADC/109/C/S1/03")
