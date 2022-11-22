# Cafe-App-Project

> A client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders.

## Client Requirements

As a business:
- I want to. maintain a collection of products and couriers.
- When a customer makes a new order, I need to create this on the system.
- I need to be able to update the status of an order i.e: preparing, out-for-delivery, delivered.
- When I exit myapp, I need all data to be persisted and not lost.
- When I start myapp, I need to. load all persisted data.
- I need  to be sure my app has been tested and proven to work well.
- I need  to receive regular software updates.

## Project Structure and D


### Mini Project Week 1

In this first week, the foundation of the app was built, in particular, the UI aspect to print to the screen, accept user input, and create a basic list data structure. The main menu and product menu options were created. Below is the week one code:

```python
"""
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
                print('\n')
                print(f'You entered {user}. The product menu options are: ')
                p_menu.get_product_menu()

    def exit_app(self):
        print('You have \x1B[1m EXITED \x1B[0m the App. \n')
        quit()

exit = 'exit'
menu_option = ['EXIT', 'PRODUCTS']
m_menu = MainMenu(exit, menu_option)

class ProductMenu():
    def __init__(self, product_menu):
        self.product_menu = product_menu
        self.products_list = products_list

    def get_product_menu(self):
        print('\n')
        print('*' * 5 + ' ' + 'PRODUCT MENU:' + ' ' + '*' * 5 + '\n')
        for i, option in enumerate(product_menu):
            print(f'{i} -> {option}')
            print(' ') 
        
        user_p = int(input('Enter a product menu option: '))
        if user_p == 0:
            print('\n' + f'You entered {user_p}. You have returned to the main menu!')
        if user_p == 1:
            p_menu.get_product_list()
        elif user_p == 2:
            print(f'you entered {user_p}.')
            p_menu.create_new_product()
        elif user_p == 3:
            p_menu.update_product()
        elif user_p == 4:
            print(f'You entered {user_p}: "delete"')
            p_menu.delete_product()

    def get_product_list(self):
        for i, option in enumerate(products_list):
            print(f'{i} -> {option}')
            print(' ')
        p_menu.get_product_menu()

    def create_new_product(self):
        print('Create a new product you want to add to the product list...')
        user_new = input('Enter a new product name: ')    
        print('you created a new product - ', 'Name: ', user_new)
        self.products_list.append(user_new)
        print('Product Successfully Added!')
        p_menu.get_product_menu()

    def update_product(self):
        print('This are the list of products we have below: ')
        for i, option in enumerate(products_list):
            print(f'{i} -> {option}')
            print(' ')
        print('If you want to update a product, ')
        user_pro_num = int(input('Enter an index value of the product you want to update: '))
        user_pro_name = input('Enter name of new product you want to update: ')      
        self.products_list[user_pro_num] = user_pro_name
        p_menu.get_product_menu()

    def delete_product(self):
        print('This are the list of products we have below: ')
        for i, option in enumerate(products_list):
            print(f'{i} -> {option}')
            print(' ')
        print('If you want to delete a product, ')
        user_pro_num = int(input('Enter an index value of the product you want to update: '))
        del self.products_list[user_pro_num]
        print('Product Deleted')
        print('This are the list of products remaining: ')
        for i, option in enumerate(products_list):
            print(f'{i} -> {option}')
            print(' ')
        p_menu.get_product_menu()

products_list = ['Chicken Pie', 'Curry Rice', 'Cottage Pie', 'Coke', 'Fanta']
product_menu = ['MAIN MENU', 'PRODUCT LIST', 'CREATE', 'UPDATE', 'DELETE']
p_menu = ProductMenu(product_menu)
m_menu.get_main_menu()

"""
```


### Mini Project Week 2
In week 2, order menu option was included with the order list as dictionary containing customer name, address and phone number. the code will be able to print order list, create new orders, update existing order and delete orders just as with the product menu. order menu code is shown below:

## Mini Project Week 3

## Mini Project Week 4

## Mini Project Week 5

## Mini Project Week 6
