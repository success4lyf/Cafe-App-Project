################  PROJECT ######################

##### MINI PROJECT 1 #####
main_menu = ['exit', 'product_menu', ]
products = ['rice', 'beans', 'pasta', 'egg', 'potatoes']
product_menu = ['main_menu', 'product_list', 'create', 'update', 'delete']

def get_main_menu():
    print('Welcome! The main menu options are: ')
    for i, menu in enumerate(main_menu):
        print(f'{i} = {menu}')
    
    user = int(input('enter an option from the main menu:'))
    if user == 0:
        print(f'you entered {user}. exit app')
        quit()               
    elif user == 1:
        print(f'You entered {user}. The product menu options are: ')
        get_product_menu()
    
def get_product_menu():
    for i, option in enumerate(product_menu):
        print(f'{i}: {option}')

    user_p = int(input('enter a product menu option:'))
    if user_p == 0:
        print(f'You entered {user_p}. You have returned to the main menu!')
        get_main_menu()      
    elif user_p == 1:
        product_list()        
    elif user_p == 2:
        print(f'you entered {user_p}.')
        create_new()       
    elif user_p == 3:
        update()       
    elif user_p == 4:
        print(f'You entered {user_p}: "delete"')
        delete()        
    else:
        print('invalid input')
        get_product_menu()  

def product_list():
    print('The product lists are: ')       
    print(products)
    #create_new()

def create_new():
    print('Create a new product you want to add to the product list...')
    user_new = input('Enter a new product name: ')
    products.append(user_new)
    print('you created a new product: ', user_new)
    print('New product list = ', products)
    #update()

def update():
    print('This are the list of products we have below: ')
    for i, product in enumerate(products):
        print(f'{i}: {product}')
    print('If you want to update a product, ')
    user_num = int(input('Enter an index value of the product: '))
    user_name = input('Enter a product name: ')
    try:
        products[user_num] = user_name
        print('The updated product list is: ')
        print(products)
        delete()
    except IndexError:
        print('Number Out of range. Try again.')
        update()

def delete():
    print('The product list are: ')
    print(products)
    print('you can choose the product to delete now!')
    user_del = int(input('Enter an index value of the product you want to delete: '))
    del products[user_del]
    print('Deleted!. The products remaining are: ')
    print(products)
    get_main_menu()
   
get_main_menu()
    