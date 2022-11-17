### MINI PROJECT WEEK 3 #####

import csv

class CourierMenu():
    def __init__(self, courier_menu):
        self.courier_menu = courier_menu
        self.couriers_list = []

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
            c_menu.load_couriers()
            break
        c_menu.get_courier_menu()

    def create_new_couirer(self):
        print('Create a new courier you want to add to the courier list...')
        user_cou_name = input('Enter a new courier name: ')
        user_cou_num = input('Enter the courier phone number: ')
        print('you created a new courier - ', {'Name': user_cou_name, 'Phone Num': user_cou_num})
        with open('file_content/courier.csv', 'a') as file:
            fieldnames = ['NAME', 'PHONE NUM']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'NAME': user_cou_name, 'PHONE NUM': user_cou_num})
        file.close()
        print('Courier Successfully Added!')
        c_menu.get_courier_menu()

    def update_courier(self):
        while True:
            print('This are the list of couriers we have below: ')
            c_menu.load_couriers()
            print('If you want to update a courier, ')
            user_co_num = int(input('Enter an index value of the courier you want to update: '))       
            if user_co_num > len(self.couriers_list):
                print('Out of range, Try again!')
                continue

            else:
                print('Do you want to update this courier - ', self.couriers_list[user_co_num], '?')
                answer = input("Enter 'y' for YES and 'n' for NO: " )
                if answer == 'y':
                    key_value = input("Enter value if 'NAME' or 'PHONE NUM' you want to update: ")       
                    if key_value in self.couriers_list[user_co_num]:
                        print('you want to update the product ',key_value, ' - ', (self.couriers_list[user_co_num])[key_value])
                        c_update = input('Please input the correct detail now: ')
                        (self.couriers_list[user_co_num])[key_value] = c_update
                        print('The updated detail is: ', self.couriers_list[user_co_num], '\n')
                        print(self.couriers_list)              
                        c_menu.save_couriers()
                        print('\n Update Successful!')

                        print('Do you want to update anything else? ')
                        reply = input("Enter 'y' for YES and 'n' for NO: " )
                        if reply == 'y':
                           continue
                        elif reply == 'n':
                            print('OK! You have returned to the courier menu')
                            break
                        else:
                            print('your input is blank. nothing to update')
                            break
            
                    else:
                        print('your input is blank. nothing to update')
                        break        
                elif answer == 'n':
                    print('OK! You have returned to the courier menu')
                    break
                else:
                    print('Invalid Input, Try again')
                    break
        c_menu.get_courier_menu()       

    def delete_courier(self):
        while True:
            print('The courier list are: ')
            c_menu.load_couriers()
            print('you can choose a courier to delete now!')
            user_del_co = int(input('Enter an index value of the courier you want to delete: '))
            print('You selected - ', self.couriers_list[user_del_co])
            del self.couriers_list[user_del_co]
            print('\n Selected Courier Deleted. \n The couriers remaining are: ')
            print(self.couriers_list)
            c_menu.save_couriers()
            break
        c_menu.get_courier_menu()


courier_menu = ['Main Menu', 'Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']
c_menu = CourierMenu(courier_menu)
# c_menu.get_courier_menu()