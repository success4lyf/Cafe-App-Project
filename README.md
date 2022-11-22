# Cafe-App-Project

> A client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders.

## Client Requirements

As a business:
- I want to maintain a collection of products and couriers.
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
                
            elif user == 2:
                print(f'You entered {user}. The courier menu options are: ')                
                c_menu.get_courier_menu()
                
            elif user == 3:
                print(f'You entered {user}. The order menu options are: ')
                o_menu.get_order_menu()

    def exit_app(self):
        print('You have \x1B[1m EXITED \x1B[0m the App. \n')
        quit()

exit = 'exit'
menu_option = ['EXIT', 'PRODUCTS', 'COURIER', 'ORDERS']
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

```python
"""
class OrderMenu():
    def __init__(self, order_menu):
        self.order_menu = order_menu
        self.orders_list = order_list
        self.order_status = order_status

    def get_order_menu(self):
        print('\n')
        for i, option in enumerate(order_menu):
            print(f'{i}: {option}')

        user_o = int(input('enter an order menu option:'))
        if user_o == 0:
            print(f'You entered {user_o}. You have returned to the main menu!')
        elif user_o == 1:
            o_menu.get_orders_list()      
        elif user_o == 2:
            o_menu.create_order_details()
        elif user_o == 3:
            o_menu.update_order_status()
        elif user_o == 4:
            o_menu.update_existing_orders()
        elif user_o == 5:
            o_menu.delete_order()
        else:
            print('invalid input')

    def get_orders_list(self):
        print('\n' + 'The orders list are: \n')
        for i, option in enumerate(self.orders_list):
            print(f'{i} -> {option}')
            print(' ')
        o_menu.get_order_menu()

    def create_order_details(self):
        self.orders_dict = {}
        self.order_status = order_status
        self.name = 'NAMES'
        self.address = 'ADDRESSES'
        self.phone = 'PHONE NUMBERS'
        self.status = 'ORDERS STATUS'

        print('If you want to create an order, Please enter your details.')       
        user_name = input('Enter your name: ')
        user_address = input('Enter your address: ')
        user_phone = int(input('Enter your phone number: '))
        self.orders_dict.update({self.name : user_name})
        self.orders_dict.update({self.address : user_address})
        self.orders_dict.update({self.phone : user_phone})
        self.orders_dict.update({self.status : self.order_status[0]})
        print('New Order Details = ', self.orders_dict, '\n')
        self.orders_list.append(self.orders_dict)
        print(self.orders_list)
        print('\nOrders Added')
        o_menu.get_order_menu()
        
    def update_order_status(self):
        print('\n' + 'The orders list are: \n')
        for i, option in enumerate(self.orders_list):
            print(f'{i} -> {option}')
            print(' ')
        user_ol = int(input('Enter the index number of the order list: '))
        print('you entered', user_ol)
        print(self.orders_list[user_ol])
            
        for i, status in enumerate(self.order_status):
            print(f'{i}: {status}')
        user_st = int(input('Enter the index number of the order status: '))
        self.orders_list[user_ol]['ORDERS STATUS'] = self.order_status[user_st]
        print(self.orders_list[user_ol])
        o_menu.get_order_menu()

    def update_existing_orders(self):
        print('\n' + 'The orders list are: \n')
        for i, option in enumerate(self.orders_list):
            print(f'{i} -> {option}')
            print(' ')
        user_ol = int(input('Enter the index number of the order you want to update: '))
        print(self.orders_list[user_ol])
        key_value = input("Enter what you want to update eg: 'NAME' or 'ADDRESS': ")       
        if key_value in self.orders_list[user_ol]:
            print('you want to update the your ',key_value, ' - ', (self.orders_list[user_ol])[key_value])
            o_update = input('Please input the correct detail now: ')
            (self.orders_list[user_ol])[key_value] = o_update
            print('The updated detail is: ', self.orders_list[user_ol], '\n')
            print(self.orders_list)  
            print('\n Update Successful!')
        else:
            print('your input is incorrect!. nothing to update. \nyou have returned to the order menu')
        o_menu.get_order_menu()

    def delete_order(self):
        print('\n' + 'The orders list are: \n')
        for i, option in enumerate(self.orders_list):
            print(f'{i} -> {option}')
            print(' ')
        print('you can choose a order details to delete now!')
        user_or_del = int(input('Enter an index value of the order you want to delete: '))
        print('\n You selected - ', self.orders_list[user_or_del])
        del self.orders_list[user_or_del]
        print('\n Selected Order Deleted.  The orders remaining are: \n')
        print(self.orders_list)
        o_menu.get_order_menu()
        
order_list = [{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "status": "preparing"
}, {
  "customer_name": "James",
  "customer_address": "Unit 7, 19 Main Street, LONDON, WC8 2UR",
  "customer_phone": "07898567437",
  "status": "preparing"
}]
order_menu = ['Main Menu', 'Order Details', 'Add Order Details',  'Update Existing Order Status', 'Update Existing Order', 'Delete Order']
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
o_menu = OrderMenu(order_menu)
        
"""
```

### Mini Project Week 3

In this week, the courier menu option was created to allow user add, update and delete courier. Also the product list, courier list and order list was saved in a txt file.

### Mini Project Week 4

In week 4, instead of loading data from txt file, data was loaded and saved from csv file for product list, courier list and orders list. the code for loading and saving of product list from csv file is shown below, which is same for both courier and orders list. this function is called in all the menu  options to load and save files.

```python
"""
def load_products(self):
        with open('file_content/product.csv', 'r') as file:
            dict_reader = csv.DictReader(file)
            self.products_list = list(dict_reader)
            for i, row in enumerate(self.products_list):
                print('\t' + f'{i}: {row} \n')
        file.close()

    def save_products(self):
        with open('file_content/product.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['NAME', 'PRICE'])
            for product in self.products_list:
                writer.writerow(product.values())
        file.close()
"""
```

## Mini Project Week 5

In week 5, the data is stored in the database instead of csv file. pymysql is used to connect to mysql database. Product, Courier, Order and Order status tables were created with pymysql connector and data from the table was fetched, inserted, updated and deleted in the code. In the main branch of this project you will see the code for loading the csv file to the database after converting it to dataframe using pandas and then creating tables in the database. Below is the image of the database for product table:



## Mini Project Week 6
