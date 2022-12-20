import csv
import pymysql
import os
from dotenv import load_dotenv

class CourierMenu():
    def __init__(self, courier_menu):
        self.courier_menu = courier_menu
        self.couriers_list = []

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

    def get_couriers_from_sql(self):
        self.cursor.execute('SELECT * FROM couriers')
        rows = self.cursor.fetchall()
        for row in rows:
            print(f'COURIER_ID: {str(row[0])}, COURIER_NAME: {str(row[1])}, PHONE_NUM: {str(row[2])}')

    def load_couriers(self):
        with open('file_content/courier.csv', 'r') as file:
            dict_reader = csv.DictReader(file)
            self.couriers_list = list(dict_reader)
            for i, row in enumerate(self.couriers_list):
                print('\t' + f'{i}: {row} \n')
        file.close()

    def save_couriers(self):
        with open('file_content/courier.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['NAME', 'PHONE NUM'])
            for courier in self.couriers_list:
                writer.writerow(courier.values())
        file.close()

    def get_courier_menu(self):
        for i, courier in enumerate(courier_menu):
            print(f'{i}: {courier}')

        user_c = int(input('Enter the index value of the courier menu option: '))
        if user_c == 0:
            print('\n' + f'You entered {user_c}. You have returned to the main menu!')
        elif user_c == 1:
            c_menu.get_courier_list()
        elif user_c == 2:
            c_menu.create_new_couirer()
        elif user_c == 3:
            c_menu.update_courier()
        elif user_c == 4:
            c_menu.delete_courier()

    def get_courier_list(self):
        while True:
            print('The couriers list are: ')
            c_menu.get_couriers_from_sql()
            break
        c_menu.get_courier_menu()

    def create_new_couirer(self):
        print('Create a new courier you want to add to the courier table.')
        user_new = input('Enter a new courier name: ')
        user_pho = input('Enter the phone number: ')        
        print('you created a new courier - ', 'Courier Name: ',user_new, ',', 'Phone: ',user_pho)
        sql = "INSERT INTO couriers (COURIER_NAME, PHONE_NUM) VALUES (%s, %s)"
        val = (user_new, user_pho)
        self.cursor.execute(sql, val)
        self.connection.commit()
        print(self.cursor.rowcount, "record inserted.")
        print('Courier Successfully Added!')
        c_menu.get_courier_menu()

    def update_courier(self):
        while True:
            print('This are the list of couriers we have below: \n')
            c_menu.get_couriers_from_sql()
            print('If you want to update a courier, \n')
            user_cou_id = input('Enter the courier id you want to update: ')
            user_cou_name = input('Enter the name of the courier you want to update: ')
            user_cou_pho = input('Enter the phone number of the courier: ')
            if user_cou_id == "":
                print(' \n Your input for courier id is blank, No updates recorded.')
                break
            elif user_cou_name == "":
                print(' \n Your input for courier name is blank, No updates recorded.')
                break
            elif user_cou_pho == "":
                print(' \n Your input for courier phone number is blank, No updates recorded.')
                break
            else:
                print('You want to update courier id -', user_cou_id, 'with new courier name -', user_cou_name, 'and new phone number -', user_cou_pho, '\n')
                sql = "UPDATE couriers SET COURIER_NAME = %s, PHONE_NUM = %s WHERE COURIER_ID = %s"
                val = (user_cou_name, user_cou_pho, user_cou_id)
                self.cursor.execute(sql, val)
                self.connection.commit()
                print(self.cursor.rowcount, "record(s) affected")
                print('Details Updated Successfully!.')
                break
        c_menu.get_courier_menu()       

    def delete_courier(self):
        while True:
            print('\n The couriers list are: \n')
            c_menu.get_couriers_from_sql()
            print('\n You can choose the courier to delete now! \n')
            user_co_del = input('Enter the courier id you want to delete: \n')
            print('You selected courier id - ', user_co_del)
            sql = "DELETE FROM couriers WHERE COURIER_ID = %s"
            val = (user_co_del)
            self.cursor.execute(sql, val)
            self.connection.commit()
            print(self.cursor.rowcount, "record(s) deleted")
            break
        c_menu.get_courier_menu()


courier_menu = ['Main Menu', 'Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']
c_menu = CourierMenu(courier_menu)
# c_menu.get_courier_menu()
