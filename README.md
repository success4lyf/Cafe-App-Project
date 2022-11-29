# Cafe-App-Project

> A client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders.

## Client Requirements

As a business:
- I want to maintain a collection of products and couriers.
- When a customer makes a new order, I need to create this on the system.
- I need to be able to update the status of an order i.e: preparing, out-for-delivery, delivered.
- When I exit myapp, I need all data to be persisted and not lost.
- When I start myapp, I need to. load all persisted data.
- I need  to be sure my app has been tested and proven to work well.
- I need  to receive regular software updates.

## Project Structure and D


### Mini Project Week 1

In this first week, the foundation of the app was built, in particular, the UI aspect to print to the screen, accept user input, and create a basic list data structure. The main menu and product menu options were created. Below is the week one code:


### Mini Project Week 2
In week 2, order menu option was included with the order list as dictionary containing customer name, address and phone number. the code will be able to print order list, create new orders, update existing order and delete orders just as with the product menu. order menu code is shown below:


### Mini Project Week 3

In this week, the courier menu option was created to allow user add, update and delete courier. Also the product list, courier list and order list was saved in a txt file.

### Mini Project Week 4

In week 4, instead of loading data from txt file, data was loaded and saved from csv file for product list, courier list and orders list. the code for loading and saving of product list from csv file is shown below, which is same for both courier and orders list. this function is called in all the menu  options to load and save files.

```python
"""
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
"""
```

### Mini Project Week 5

In week 5, the data is stored in the database instead of csv file. pymysql is used to connect to mysql database. Product, Courier, Order and Order status tables were created with pymysql connector and data from the table was fetched, inserted, updated and deleted in the code. In the main branch of this project you will see the code for loading the csv file to the database after converting it to dataframe using pandas and then creating tables in the database. Below is the image of the database for product table:

<img width="673" alt="Screenshot 2022-11-22 at 19 40 50" src="https://user-images.githubusercontent.com/78314396/203407975-6b2dee87-8245-48c8-b3b9-59d4c8ad8435.png">

### Mini Project Week 6

The final code is refactored and unit testing is done on the code to ensure quality of the code and that the app is working. the final code code can be found in the main branch for this repository. I have done little testing on the main menu app with unittest framework. Testing is difficult to implement and i am still learning how to implement unittest and pytest in my code to make sure every unit of code works fine.
