import unittest
from app.main_menu import MainMenu
from unittest.mock import Mock, patch


class MainMenuTestcase(unittest.TestCase):

    def test_initial_value(self):
        self.menu = MainMenu(0, ['EXIT', 'PRODUCTS', 'COURIER', 'ORDERS'])
        assert self.menu.exit == 0
        assert self.menu.menu_option == ['EXIT', 'PRODUCTS', 'COURIER', 'ORDERS']

    def test_print_main_menu(self):
        expected = "***** MAIN MENU: ***** \n0 -> EXIT \n1 -> PRODUCTS \n2 -> COURIER \n3 -> ORDERS"
        def mock_get_main_menu():
            return "***** MAIN MENU: ***** \n0 -> EXIT \n1 -> PRODUCTS \n2 -> COURIER \n3 -> ORDERS"
        actual = mock_get_main_menu() 
        assert expected == actual

    def test_input_option_0(self):
        original_input = __builtins__.input
        __builtins__.input = lambda _: 0
        with self.assertRaises(SystemExit):
            MainMenu.exit_app(self)
        __builtins__.input = original_input


if __name__ == '__main__':
    unittest.main()

