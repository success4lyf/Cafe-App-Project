##### MINI PROJECT WEEK 1 #####

import csv

class ProductMenu():
    def __init__(self, product_menu):
        self.product_menu = product_menu
        self.products_list = []
    
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
        while True:
            print('\n' + 'The products list and prices are: \n')
            p_menu.load_products()
            break
        p_menu.get_product_menu()

    def create_new_product(self):
        print('Create a new product you want to add to the product list...')
        user_new = input('Enter a new product name: ')
        user_price = input('Enter the price: ')        
        print('you created a new product - ', 'Name: ', user_new, ',' , 'Price: ', user_price)
        with open('file_content/product.csv', 'a') as file:
            fieldnames = ['Name', 'Price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Name': user_new, 'Price': user_price})
        file.close()
        print('Product Successfully Added!')
        p_menu.get_product_menu()

    def update_product(self):
        while True:
            print('This are the list of products we have below: ')
            p_menu.load_products()
            print('If you want to update a product, ')
            user_pro_num = int(input('Enter an index value of the product you want to update: '))       
            if user_pro_num > len(self.products_list):
                print('Out of range, Try again!')
                continue

            else:
                print('Do you want to update this product - ', self.products_list[user_pro_num], '?')
                answer = input("Enter 'y' for YES and 'n' for NO: " )
                if answer == 'y':
                    key_value = input("Enter value if 'NAME' or 'PRICE' you want to update: ")       
                    if key_value in self.products_list[user_pro_num]:
                        print('you want to update the product ',key_value, ' - ', (self.products_list[user_pro_num])[key_value])
                        p_update = input('Please input the correct detail now: ')
                        (self.products_list[user_pro_num])[key_value] = p_update
                        print('The updated detail is: ', self.products_list[user_pro_num], '\n')
                        print(self.products_list)              
                        p_menu.save_products()
                        print('\n Update Successful!')

                        print('Do you want to update anything else? ')
                        reply = input("Enter 'y' for YES and 'n' for NO: " )
                        if reply == 'y':
                           continue
                        elif reply == 'n':
                            print('OK! You have returned to the product menu')
                            break
                        else:
                            print('your input is blank. nothing to update')
                            break
            
                    else:
                        print('your input is blank. nothing to update')
                        break        
                elif answer == 'n':
                    print('OK! You have returned to the product menu')
                    break
                else:
                    print('Invalid Input, Try again')
                    break
        p_menu.get_product_menu()           

    def delete_product(self):
        while True:
            print('The product list are: ')
            p_menu.load_products()
            print('you can choose the product to delete now!')
            user_del = int(input('Enter an index value of the product you want to delete: '))
            print('You selected - ', self.products_list[user_del])
            del self.products_list[user_del]
            print('\n Selected Product Deleted. \n The products remaining are: ')
            print(self.products_list)
            p_menu.save_products()
            break
        p_menu.get_product_menu()

 
product_menu = ['MAIN MENU', 'PRODUCT LIST', 'CREATE', 'UPDATE', 'DELETE']
p_menu = ProductMenu(product_menu)
# p_menu.get_product_menu()

