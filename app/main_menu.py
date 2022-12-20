from product_menu import ProductMenu
from order_menu import OrderMenu
from courier_menu import CourierMenu

class MainMenu:
    def __init__(self, exit, menu_option):
        self.exit = exit
        self.menu_option = menu_option
        self.order_list = []
        print('\n' * 2)
        print('*' * 10 + ' ' + '\x1B[1m' + 'WELCOME TO OUR POP-UP CAFE APP!' + '\x1B[0m' + ' ' + '*' * 10)
        
    def get_main_menu(self):
        while True:
            print('\n')
            print('*' * 5 + ' ' + '\x1B[1m' + 'MAIN MENU:' + '\x1B[0m' + ' ' + '*' * 5 + '\n')
            for i, menu in enumerate(menu_option):
                print(f'{i} -> {menu}')
                print(' ')
            
            user = int(input('Enter a main menu option: '))
            if user == 0:
                print('\n' + f'You entered {user} -> {menu_option[0]}. \n')
                m_menu.exit_app()

            elif user == 1:
                print(f'\n You entered {user}. The product menu options are: ')
                ProductMenu.get_product_menu(self)         

            elif user == 2:
                print(f'You entered {user}. The courier menu options are: ')                
                CourierMenu.get_courier_menu(self)
                
            elif user == 3:
                print(f'You entered {user}. The order menu options are: ')
                OrderMenu.get_order_menu(self)

    def exit_app(self):
        print('You have \x1B[1m EXITED \x1B[0m the App. \n')
        quit()

if __name__ == "__main__":
    exit = 'exit'
    menu_option = ['EXIT', 'PRODUCTS', 'COURIER', 'ORDERS']
    m_menu = MainMenu(exit, menu_option)
    m_menu.get_main_menu()
    