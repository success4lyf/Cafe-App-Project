##### MINI PROJECT WEEK 2 #####
from product_menu import ProductMenu
from courier_menu import CourierMenu
import csv

class OrderMenu():
    def __init__(self, order_menu):
        self.order_menu = order_menu
        self.orders_list = []
        self.order_status = order_status

    def load_orders(self):
        with open('file_content/orders.csv', 'r') as file:
            dict_reader = csv.DictReader(file)
            self.orders_list = list(dict_reader)
            for i, row in enumerate(self.orders_list):
                print('\t' + f'{i}: {row} \n')
        file.close()

    def save_orders(self):
        with open('file_content/orders.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['NAMES', 'ADDRESSES', 'PHONE NUMBERS', 'COURIERS', 'ORDERS STATUS', 'PRODUCT ITEMS'])
            for order in self.orders_list:
                writer.writerow(order.values())
        file.close()
    
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
        while True:
            print('\n' + 'The orders list are: \n')
            o_menu.load_orders()
            break
        o_menu.get_order_menu()

    def create_order_details(self):
        self.orders_dict = {}
        self.ordered_products = []
        self.name = 'NAMES'
        self.address = 'ADDRESSES'
        self.phone = 'PHONE NUMBERS'
        self.courier = 'COURIERS'
        self.status = 'ORDERS STATUS'
        self.product_items = 'PRODUCT ITEMS'

        print('If you want to create an order, Please enter your details.')       
        user_name = input('Enter your name: ')
        user_address = input('Enter your address: ')
        user_phone = int(input('Enter your phone number: '))

        while True:
            print('\n This are the list of products we have -: \n')
            ProductMenu.load_products(self)
            user_products = int(input('Select the index number of the products you want to order: '))
            self.ordered_products.append(user_products)
            print('Do you want to add another products?')
            answer = input("Enter 'y' for YES and 'n' for NO: " )
            if answer == 'y':
                continue
            elif answer == 'n':
                print('Thank You')
                print('Ordered Products are index no -> ', self.ordered_products)
                product_result = ','.join(map(str, self.ordered_products))
                # print(product_result)
                break
        print('\n This are the available couriers below:  \n')
        CourierMenu.load_couriers(self)
        user_courier = int(input('Select the index number of the courier you want to use: '))
        status = self.order_status[0]

        self.orders_dict.update({self.name : user_name})
        self.orders_dict.update({self.address : user_address})
        self.orders_dict.update({self.phone : user_phone})
        self.orders_dict.update({self.courier : user_courier})
        self.orders_dict.update({self.product_items : product_result})
        self.orders_dict.update({self.status : status})
        print('New Order Details = ', self.orders_dict)

        with open('file_content/orders.csv', 'a') as file:
            fieldnames = ['NAMES', 'ADDRESSES', 'PHONE NUMBERS', 'COURIERS', 'ORDERS STATUS', 'PRODUCT ITEMS']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow( self.orders_dict)
        file.close()
        o_menu.get_order_menu()

    def update_order_status(self):
        while True:
            o_menu.load_orders()  
            user_ol = int(input('Enter the index number of the order list: '))
            print('you entered', user_ol)
            print(self.orders_list[user_ol])
            
            for i, status in enumerate(self.order_status):
                print(f'{i}: {status}')
            user_st = int(input('Enter the index number of the order status: '))
            self.orders_list[user_ol]['ORDERS STATUS'] = self.order_status[user_st]
            print(self.orders_list[user_ol])
            o_menu.save_orders()
            break
        o_menu.get_order_menu()

    def update_existing_orders(self):
        while True:
            o_menu.load_orders()
            user_ol = int(input('Enter the index number of the order you want to update: '))
            if user_ol > len(self.orders_list):
                    print('Out of range, Try again!')
                    continue

            else:
                print('Do you want to update this order - ', self.orders_list[user_ol], '?')
                answer = input("Enter 'y' for YES and 'n' for NO: " )
                if answer == 'y':
                    key_value = input("Enter what you want to update eg: 'NAME' or 'ADDRESS': ")       
                    if key_value in self.orders_list[user_ol]:
                        print('you want to update the your ',key_value, ' - ', (self.orders_list[user_ol])[key_value])
                        o_update = input('Please input the correct detail now: ')
                        (self.orders_list[user_ol])[key_value] = o_update
                        print('The updated detail is: ', self.orders_list[user_ol], '\n')
                        # print(self.orders_list)              
                        o_menu.save_orders()
                        print('\n Update Successful!')

                        print('Do you want to update anything else? ')
                        reply = input("Enter 'y' for YES and 'n' for NO: " )
                        if reply == 'y':
                            continue
                        elif reply == 'n':
                            print('OK! You have returned to the order menu')
                            break
                        else:
                            print('your input is blank. nothing to update')
                            break
                
                    else:
                        print('your input is blank. nothing to update')
                        break        
                elif answer == 'n':
                    print('OK! You have returned to the order menu')
                    break
                else:
                    print('Invalid Input, Try again')
                    break
        o_menu.get_order_menu()

    def delete_order(self):
        while True:
            print('The order list are: ')
            o_menu.load_orders()
            print('you can choose a order details to delete now!')
            user_or_del = int(input('Enter an index value of the order you want to delete: '))
            print('\n You selected - ', self.orders_list[user_or_del])
            del self.orders_list[user_or_del]
            print('\n Selected Order Deleted.  The orders remaining are: \n')
            print(self.orders_list)
            o_menu.save_orders()
            break
        o_menu.get_order_menu()


order_menu = ['Main Menu', 'Order Details', 'Add Order Details',  'Update Existing Order Status', 'Update Existing Order', 'Delete Order']
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

o_menu = OrderMenu(order_menu)
# o_menu.get_order_menu()

