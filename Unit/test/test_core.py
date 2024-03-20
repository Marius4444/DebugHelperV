import sys

sys.path.append('path/to/your/module')

from unittest.mock import patch

from core import show_menu


def test_show_menu_main():
  # Mock input to return '1' and capture print statements
  with patch('builtins.input' , return_value='1') , patch(
      'builtins.print') as mocked_print:
    assert show_menu("main") == '1'
    
    mocked_print.assert_any_call(
        '\nWelcome to the Debug Helper. Please choose the module as fallow ')
    
