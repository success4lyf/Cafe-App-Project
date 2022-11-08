################  PROJECT ######################

##### MINI PROJECT 2 #####

class App:
    def __init__(self, exit, main_menu):
        self.exit = exit
        self.main_menu = main_menu

    def get_main_menu(self):
        print('Welcome! The main menu options are: ')
        for i, menu in enumerate(main_menu):
            print(f'{i} = {menu}')

        user = int(input('enter an option from the main menu:'))
        if user == 0:
            print(f'you entered {user}.')
            print('exit app')
            p_menu.exit_app()    
        elif user == 1:
            print(f'You entered {user}. The product menu options are: ')
            p_menu.get_product_menu()
        elif user == 2:
            print(f'You entered {user}. The order menu options are: ')
            o_menu.get_order_menu()
    
    def exit_app(self):
        print('You have exited the from the App.')
        quit()

class ProductMenu(App):
    def __init__(self, exit, main_menu, products, product_menu, order_menu):
        super().__init__(exit, main_menu)       
        self.products = products
        self.product_menu = product_menu
        self.order_menu = order_menu
        
    def get_product_menu(self):
        for i, option in enumerate(product_menu):
            print(f'{i}: {option}')
        
        user_p = int(input('enter a product menu option:'))
        if user_p == 0:
            print(f'You entered {user_p}. You have returned to the main menu!')
            p_menu.get_main_menu()
        elif user_p == 1:
            p_menu.get_product_list()
        elif user_p == 2:
            print(f'you entered {user_p}.')
            p_menu.create_new_product()
        elif user_p == 3:
            p_menu.update_product()
        elif user_p == 4:
            print(f'You entered {user_p}: "delete"')
            p_menu.delete_product()
        else:
            print('invalid input')
            p_menu.get_product_menu()

    def get_product_list(self):
        print('The product lists are: ')       
        print(products)

    def create_new_product(self):
        print('Create a new product you want to add to the product list...')
        user_new = input('Enter a new product name: ')
        products.append(user_new)
        print('you created a new product: ', user_new)
        print('New product list = ', products)

    def update_product(self):
        print('This are the list of products we have below: ')
        for i, product in enumerate(products):
            print(f'{i}: {product}')
        print('If you want to update a product, ')
        user_pro_num = int(input('Enter an index value of a product: '))
        user_pro_name = input('Enter a product name: ')
        products[user_pro_num] = user_pro_name
        print('The updated product list is: ')
        print(products)

    def delete_product(self):
        print('The product list are: ')
        print(products)
        print('you can choose the product to delete now!')
        user_del = int(input('Enter an index value of the product you want to delete: '))
        del products[user_del]
        print('The products remaining are: ')
        print(products)

class OrderMenu(App):
    def __init__(self, exit, main_menu, orders_dict, create_order, update_order, delete_order):
        super().__init__(exit, main_menu)
    
    def get_order_menu(self):
        for i, option in enumerate(order_menu):
            print(f'{i}: {option}')

        user_o = int(input('enter an order menu option:'))
        if user_o == 0:
            print(f'You entered {user_o}. You have returned to the main menu!')
            p_menu.get_main_menu()
        elif user_o == 1:
            print(orders_dict)
        elif user_o == 2:
            o_menu.get_order_details()
        elif user_o == 3:
            o_menu.update_orders_status()
        elif user_o == 4:
            o_menu.update_orders()
        elif user_o == 5:
            o_menu.delete_order()
        else:
            print('invalid input')

    def get_order_details(self):
        self.orders_dict = orders_dict
        self.order_status = order_status
        self.order_list = orders_list
        self.name = 'Name'
        self.address = 'Address'
        self.phone = 'Phone Num'
        self.status = 'Order Status'

        print('Please enter your details.')       
        user_name = input('Enter your name: ')
        user_address = input('Enter your address: ')
        user_phone = int(input('Enter your phone number: '))
        self.orders_dict.update({self.name : user_name})
        self.orders_dict.update({self.address : user_address})
        self.orders_dict.update({self.phone : user_phone})
        self.orders_dict.update({self.status : self.order_status[0]})
        self.order_list.append(self.orders_dict)       

    def update_orders_status(self):
        for i, order in enumerate(orders_list):
            print(f'{i} = {order}')    
        user_ol = input('Enter the index number of the order list: ')
        
        for i, status in enumerate(order_status):
            print(f'{i} = {status}')
        user_st = input('Enter the index number of the order status: ')
        #update status for order

    def update_orders(self):
        for i, order in enumerate(orders_list):
            print(f'{i} = {order}')
        user_ol = input('Enter the index number of the order list: ')

    def delete_order(self):
        pass

    

exit = 0
main_menu = ['exit', 'product_menu', 'order_menu']
products = ['rice', 'beans', 'pasta', 'egg', 'potatoes']
product_menu = ['main_menu', 'product_list', 'create', 'update', 'delete']
order_menu = ['main_menu', 'orders_dict', 'creare order',  'update order', 'delete order']
orders_dict = {}
orders_list = []
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
# order_lists = [{orders_dict}, {orders_dict}]

p_menu = ProductMenu(exit, main_menu, products, product_menu, order_menu)
o_menu = OrderMenu()
#p_menu.get_main_menu()



