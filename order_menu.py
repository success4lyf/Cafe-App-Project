import csv
import pymysql
import os
from dotenv import load_dotenv
from product_menu import ProductMenu
from courier_menu import CourierMenu


class OrderMenu():
    def __init__(self, order_menu):
        self.order_menu = order_menu
        self.orders_list = []

        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")

        self.connection = pymysql.connect(
            host,
            user,
            password,
            database
        )

        self.cursor = self.connection.cursor()

    def get_orders_from_sql(self):
        self.cursor.execute('SELECT * FROM orders')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f'ORDER_ID: {str(row[0])}, CUSTOMER_NAME: {str(row[1])}, CUSTOMER_ADDRESS: {str(row[2])}, CUSTOMER_PHONE: {str(row[3])}, PRODUCT_ITEMS: {str(row[4])}, COURIER_ID: {str(row[5])}, ORDER_STATUS_ID: {str(row[6])}')

    def get_order_status_from_sql(self):
        self.cursor.execute('SELECT * FROM order_status')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f'ORDER_STATUS_ID: {str(row[0])}, ORDER_STATUS: {str(row[1])}')


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
        print('\n The order menu options are: \n')
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
            o_menu.get_orders_from_sql()
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
            ProductMenu.get_products_from_sql(self)
            print('\n')
            user_products = input('Select the product id of the products you want to order: ')
            self.ordered_products.append(user_products)
            print('Do you want to add another products?')
            answer = input("Enter 'y' for YES and 'n' for NO: " )
            if answer == 'y':
                continue
            elif answer == 'n':
                print('Thank You')
                print('Ordered Products are product id no -> ', self.ordered_products)
                product_result = ','.join(map(str, self.ordered_products))
                print(product_result)
                break
        print('\n This are the available couriers below:  \n')
        CourierMenu.get_couriers_from_sql(self)
        user_courier = input('Select the courier id of the courier you want to use: ')
        self.cursor.execute("SELECT ORDER_STATUS_ID FROM order_status")
        status = self.cursor.fetchone()
        
        self.orders_dict.update({self.name : user_name})
        self.orders_dict.update({self.address : user_address})
        self.orders_dict.update({self.phone : user_phone})
        self.orders_dict.update({self.courier : user_courier})
        self.orders_dict.update({self.product_items : product_result})
        self.orders_dict.update({self.status : status})
        print('New Order Details = ', self.orders_dict)

        sql = "INSERT INTO orders (CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE, PRODUCT_ITEMS, COURIER_ID, ORDER_STATUS_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (user_name, user_address, user_phone,product_result, user_courier, status)
        self.cursor.execute(sql, val)
        self.connection.commit()
        print(self.cursor.rowcount, "record inserted.")
        print('Order Successfully Added!')
        o_menu.get_order_menu()

    def update_order_status(self):
        while True:
            o_menu.get_orders_from_sql()
            print('\n')  
            user_ol = input('Enter the order id number from the order list: ')
            print('you entered order id number -', user_ol, 'which is: ')
            sql = "SELECT * FROM orders WHERE ORDER_ID = %s"
            val = (user_ol)
            self.cursor.execute(sql, val)
            order_id = self.cursor.fetchall()
            print(order_id, '\n')
            
            print('The order status are: \n')
            o_menu.get_order_status_from_sql()
            user_st = input('Enter the order status id number from the order status: ')
            sql = "UPDATE orders SET ORDER_STATUS_ID = %s WHERE ORDER_ID = %s"
            val = (user_st, user_ol)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print(self.cursor.rowcount, "record(s) affected")
            print('Details Updated Successfully!.')
            break
        o_menu.get_order_menu()

    def update_existing_orders(self):
        self.ordered_products = []
        while True:
            print('This are the list of orders we have below: \n')
            o_menu.get_orders_from_sql()
            print('\n If you want to update a product, \n')
            user_id = input('Enter the order id number of the order you want to update: ')
            user_name = input('Enter your name: ')
            user_address = input('Enter your address: ')
            user_phone = input('Enter your phone number: ')

            while True:
                print('\n This are the list of products we have -: \n')
                ProductMenu.get_products_from_sql(self)
                print('\n')
                user_products = input('Select the product id of the products you want to order: ')
                self.ordered_products.append(user_products)
                print('Do you want to add another products?')
                answer = input("Enter 'y' for YES and 'n' for NO: " )
                if answer == 'y':
                    continue
                elif answer == 'n':
                    print('Thank You')
                    print('Ordered Products are product id no -> ', self.ordered_products)
                    product_result = ','.join(map(str, self.ordered_products))
                    break

            print('\n This are the available couriers below:  \n')
            CourierMenu.get_couriers_from_sql(self)
            user_courier = input('Select the courier id of the courier you want to use: ')
            self.cursor.execute("SELECT ORDER_STATUS_ID FROM order_status")
            status = self.cursor.fetchone()

            if user_id == "":
                print(' \n Your input for order id is blank, No updates recorded.')
                break
            elif user_name == "":
                print(' \n Your input for your name is blank, No updates recorded.')
                break
            elif user_address == "":
                print(' \n Your input for your address is blank, No updates recorded.')
                break
            elif user_phone == "":
                print(' \n Your input for your phone number is blank, No updates recorded.')
                break            
            else:
                print('You want to update order id:', user_id, 'with Name:', user_name, 'Address:', user_address, 'Phone no:', user_phone, 'Product id:', product_result, 'and Courier:', user_courier, '\n')
                
                sql = "UPDATE orders SET CUSTOMER_NAME = %s, CUSTOMER_ADDRESS = %s, CUSTOMER_PHONE = %s, PRODUCT_ITEMS = %s, COURIER_ID = %s, ORDER_STATUS_ID = %s WHERE ORDER_ID = %s"
                val = (user_name, user_address, user_phone, product_result, user_courier, status, user_id)
                self.cursor.execute(sql, val)
                self.connection.commit()
                print(self.cursor.rowcount, "record(s) affected")
                print('Details Updated Successfully!.')
                break
        o_menu.get_order_menu()

    def delete_order(self):
        while True:
            print('The order list are: ')
            o_menu.get_orders_from_sql()
            print('you can choose a order details to delete now!')
            user_or_del = input('Enter the order id of the order you want to delete: ')
            print('\n You selected - ', user_or_del)
            sql = "DELETE FROM orders WHERE ORDER_ID = %s"
            val = (user_or_del)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print(self.cursor.rowcount, "record(s) deleted")
            break
        o_menu.get_order_menu()


order_menu = ['Main Menu', 'Order Details', 'Add Order Details',  'Update Existing Order Status', 'Update Existing Order', 'Delete Order']
o_menu = OrderMenu(order_menu)
# o_menu.get_order_menu()