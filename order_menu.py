##### MINI PROJECT WEEK 2 #####

class OrderMenu():
    def __init__(self, order_menu):
        self.order_menu = order_menu
        #super().__init__(exit, main_menu)
    
    def get_order_menu(self):
        for i, option in enumerate(order_menu):
            print(f'{i}: {option}')

        user_o = int(input('enter an order menu option:'))
        if user_o == 0:
            print(f'You entered {user_o}. You have returned to the main menu!')
        elif user_o == 1:
            if orders_dict == {}:               
                print('Orders : ', orders_dict)
                print('No order details added. You can now add your details!')
                o_menu.get_order_details()
            else:
                print('The current orders are: ', orders_dict)
                o_menu.get_order_details()      
        elif user_o == 2:
            o_menu.get_order_details()
        elif user_o == 3:
            o_menu.update_order_status()
        elif user_o == 4:
            o_menu.update_existing_orders()
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
        print('Order Details = ', orders_dict)
        print('List of Orders = ', self.order_list)
        o_menu.get_order_menu()    

    def update_order_status(self):
        self.order_status = order_status
        for i, order in enumerate(orders_list):
            print(f'{i} = {order}')    
        user_ol = int(input('Enter the index number of the order list: '))
        print('you entered', user_ol)
        print(orders_list[user_ol])
        
        for i, status in enumerate(order_status):
            print(f'{i}: {status}')
        user_st = int(input('Enter the index number of the order status: '))
        orders_list[user_ol]['Order Status'] = self.order_status[user_st]
        print(orders_list[user_ol])

    def update_existing_orders(self):
        for i, order in enumerate(orders_list):
            print(f'{i} = {order}')
        
        user_ol = int(input('Enter the index number of the order you want to update: '))
        print('Do you want to update this order - ', orders_list[user_ol], '?')
        answer = input("Enter 'y' for YES and 'n' for NO: " )
        if answer == 'y':
            print('The keys are: ')
            for key in orders_list[user_ol]:
                print(key)
            key_value = input('Enter the name of the key you want to update in the order: ')
            if key_value in orders_list[user_ol]:
                print('you want to update your', key_value, ' - ', (orders_list[user_ol])[key_value])
                o_update = input('Please input the correct details now: ')
                (orders_list[user_ol])[key_value] = o_update
                print('The updated details is: ')
                print(orders_list[user_ol])
            else:
                print('your input is blank. nothing to update')
                o_menu.get_order_menu()
        elif answer == 'n':
            print('OK! You have returned to the order menu')
            o_menu.get_order_menu()

    def delete_order(self):
        for i, order in enumerate(orders_list):
            print(f'{i} = {order}')

        user_ol = int(input('Enter the index number of the order you want to delete: '))
        del orders_list[user_ol]
        print('This are the remaining orders - ')
        print(orders_list)


order_menu = ['Main Menu', 'Order Details', 'Add Order Details',  'Update Existing Order Status', 'Update Existing Order', 'Delete Order']
orders_dict = {}
orders_list = [{
  "Name": "John",
  "Address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "Phone Num": "0789887334",
  "Order Status": "preparing"
}, {
  "Name": "James",
  "Address": "Unit 9, 19 Main Street, LONDON, WC1 2EY",
  "Phone Num": "07897643257",
  "Order Status": "preparing"
}]
order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
o_menu = OrderMenu(order_menu)

