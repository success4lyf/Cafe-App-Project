##### MINI PROJECT WEEK 1 #####

class ProductMenu():
    def __init__(self, product_menu):       
        self.product_menu = product_menu
        
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
        self.products = products
        print('\n' + 'The products list are: \n')
        for i, product in enumerate(products):            
            print('\t' + f'{i}: {product} \n')
        p_menu.get_product_menu()

    def create_new_product(self):
        print('Create a new product you want to add to the product list...')
        user_new = input('Enter a new product name: ')
        products.append(user_new)
        print('you created a new product: ', user_new)
        print('New product list = ', products)
        p_menu.get_product_menu()

    def update_product(self):
        print('This are the list of products we have below: ')
        for i, product in enumerate(products):
            print(f'{i}: {product}')
        print('If you want to update a product, ')
        user_pro_num = int(input('Enter an index value of a product: '))        
        if user_pro_num > products[0:]:
            print('out of range')
            p_menu.update_product()
        else:
            user_pro_name = input('Enter a product name: ')
            products[user_pro_num] = user_pro_name
            print('The updated product list is: ')
            print(products)
            p_menu.get_product_menu()

    def delete_product(self):
        print('The product list are: ')
        print(products)
        print('you can choose the product to delete now!')
        user_del = int(input('Enter an index value of the product you want to delete: '))
        del products[user_del]
        print('The products remaining are: ')
        print(products)
        p_menu.get_product_menu()

products = ['Rice', 'Beans', 'Pasta', 'Egg', 'Potatoes']
product_menu = ['MAIN MENU', 'PRODUCT LIST', 'CREATE', 'UPDATE', 'DELETE']
p_menu = ProductMenu(product_menu)

