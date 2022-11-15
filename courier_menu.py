### MINI PROJECT WEEK 3 #####

class CourierMenu():
    def __init__(self, courier_menu):
        self.courier_menu = courier_menu

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
        self.courier_list = courier_list
        print('The courier lists are: ')
        for i, courier in enumerate(courier_list):            
            print('\t' + f'{i}: {courier} \n')
        c_menu.get_courier_menu()

    def create_new_couirer(self):
        print('Create a new courier you want to add to the courier list...')
        user_new_co = input('Enter a new courier name: ')
        courier_list.append(user_new_co)
        print('you created a new courier: ', user_new_co)
        print('Courier list = ', courier_list)
        c_menu.get_courier_menu()

    def update_courier(self):
        print('This are the list of courier names: ')
        for i, courier in enumerate(courier_list):
            print(f'{i}: {courier}')
        print('If you want to update a courier, ')
        user_cou_num = int(input('Enter an index value of the courier name you want to update: '))        
        # if user_pro_num > products[i]:
        #     print('out of range')
        #     p_menu.update_product()
        # else:
        user_cou_name = input('Enter a product name: ')
        courier_list[user_cou_num] = user_cou_name
        print('The updated courier list is: ')
        print(courier_list)
        c_menu.get_courier_menu()

    def delete_courier(self):
        print('The courier list are: ')
        print(courier_list)
        print('you can choose the courier name you want to delete now!')
        user_del_co = int(input('Enter an index value of the courier name you want to delete: '))
        del courier_list[user_del_co]
        print('The courier names remaining are: ')
        print(courier_list)
        c_menu.get_courier_menu()
      
courier_list = [{'Name': 'UPS', 'Phone': '01623459870'}, 
                {'Name': 'DHL', 'Phone': '01642357680'}, 
                {'Name': 'Royal Mail', 'Phone': '01687659843'},
                {'Name': 'Hemes', 'Phone': '01653427156'}, 
                {'Name': 'FedEx', 'Phone': '01604827458'}]

courier_menu = ['Main Menu', 'Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']
c_menu = CourierMenu(courier_menu)