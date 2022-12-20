import csv
import pymysql
import os
from dotenv import load_dotenv

class ProductMenu():
    def __init__(self, product_menu):
        self.product_menu = product_menu
        self.products_list = []
        
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

    def get_products_from_sql(self):
        self.cursor.execute('SELECT * FROM products')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f'PRODUCT_ID: {str(row[0])}, PRODUCT_NAME: {str(row[1])}, PRICE: {str(row[2])}')

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

    def get_product_menu(self):
        print('\n' + '*' * 5 + ' ' + 'PRODUCT MENU:' + ' ' + '*' * 5 + '\n')
        for i, option in enumerate(product_menu):
            print(f'{i} -> {option} \n')
        
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
        while True:
            print('\n' + 'The products list and prices are: \n')
            p_menu.get_products_from_sql()
            break
        p_menu.get_product_menu()

    def create_new_product(self):
        print('Create a new product you want to add to the product list...')
        user_new = input('Enter a new product name: ')
        user_price = input('Enter the price: ')        
        print('you created a new product - ', 'Product Name: ', user_new, ',' , 'Price: ', user_price)
        sql = "INSERT INTO products (PRODUCT_NAME, PRICE) VALUES (%s, %s)"
        val = (user_new, user_price)
        self.cursor.execute(sql, val)
        self.connection.commit()
        print(self.cursor.rowcount, "record inserted.")
        print('Product Successfully Added!')
        p_menu.get_product_menu()

    def update_product(self):
        while True:
            print('This are the list of products we have below: \n')
            p_menu.get_products_from_sql()
            print('If you want to update a product, \n')
            user_pro_id = input('Enter the product id you want to update: ')
            user_pro_name = input('Enter the name of the product you want to update: ')
            user_pro_price = input('Enter the price of the product you want to update: ')
            if user_pro_id == "":
                print(' \n Your input for product id is blank, No updates recorded.')
                break
            elif user_pro_name == "":
                print(' \n Your input for product name is blank, No updates recorded.')
                break
            elif user_pro_price == "":
                print(' \n Your input for product price is blank, No updates recorded.')
                break
            else:
                print('You want to update product id -', user_pro_id, 'with new product name -', user_pro_name, 'and new price -', user_pro_price, '\n')
                sql = "UPDATE products SET PRODUCT_NAME = %s, PRICE = %s WHERE PRODUCT_ID = %s"
                val = (user_pro_name, user_pro_price, user_pro_id)
                self.cursor.execute(sql, val)
                self.connection.commit()
                print(self.cursor.rowcount, "record(s) affected")
                print('Details Updated Successfully!.')
                break
        p_menu.get_product_menu()

    def delete_product(self):
        while True:
            print('\n The product list are: \n')
            p_menu.get_products_from_sql()
            print('\n You can choose the product to delete now! \n')
            user_del = input('Enter the product id you want to delete: \n')
            print('You selected product id - ', user_del)
            sql = "DELETE FROM products WHERE PRODUCT_ID = %s"
            val = (user_del)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print(self.cursor.rowcount, "record(s) deleted")
            break
        p_menu.get_product_menu()


product_menu = ['MAIN MENU', 'PRODUCT LIST', 'CREATE', 'UPDATE', 'DELETE']
p_menu = ProductMenu(product_menu)
# p_menu.get_product_menu()
