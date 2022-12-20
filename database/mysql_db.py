import pandas as pd
import pymysql
import os
from dotenv import load_dotenv

class Database():
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")

        # Connect to MYSQL Server
        self.connection = pymysql.connect( 
            host, 
            user, 
            password, 
            database
            )
        # cursor object
        self.cursor = self.connection.cursor()

    def create_tables(self):
        product_table = """
            CREATE TABLE if not exists products (
                PRODUCT_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                PRODUCT_NAME NVARCHAR(50),
                PRICE DECIMAL(6,2)
                )
        """

        courier_table = """
            CREATE TABLE if not exists couriers (
                COURIER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                COURIER_NAME NVARCHAR(50),
                PHONE_NUM NVARCHAR(50)
                )
        """

        order_staus_table = """
            CREATE TABLE if not exists order_status (
                ORDER_STATUS_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                ORDER_STATUS NVARCHAR(50)
                )
        """
        
        orders_table = """
            CREATE TABLE if not exists orders (
                ORDER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                CUSTOMER_NAME NVARCHAR(50), CUSTOMER_ADDRESS NVARCHAR(250), 
                CUSTOMER_PHONE NVARCHAR(50), COURIER_ID INT NOT NULL, 
                ORDER_STATUS_ID INT NOT NULL, PRODUCT_ITEMS CHAR(50), 
                FOREIGN KEY (COURIER_ID) REFERENCES couriers(COURIER_ID) 
                    ON DELETE CASCADE, 
                FOREIGN KEY (ORDER_STATUS_ID) REFERENCES order_status(ORDER_STATUS_ID) 
                    ON DELETE CASCADE
                    )
        """
        
        self.cursor.execute(product_table)
        self.cursor.execute(courier_table)
        self.cursor.execute(order_staus_table)
        self.cursor.execute(orders_table)
        print('tables created')

    def insert_into_table(self):
    # product inserting
        data1= pd.read_csv ('file_content/product.csv')   
        df1 = pd.DataFrame(data1)
        for row in df1.itertuples():
            sql = "INSERT INTO products (PRODUCT_NAME, PRICE) VALUES (%s,%s)" 
            val = (row.PRODUCT_NAME, row.PRICE)
            self.cursor.execute(sql, val)

        #courier inserting
        data2 = pd.read_csv ('file_content/courier.csv')
        df2 = pd.DataFrame(data2)
        for row in df2.itertuples():
            sql = "INSERT INTO couriers (COURIER_NAME, PHONE_NUM) VALUES (%s,%s)" 
            val = (row.COURIER_NAME, row.PHONE_NUM)
            self.cursor.execute(sql, val)

        #order status inserting
        sql = "INSERT INTO order_status (ORDER_STATUS) VALUES (%s)"
        val = [('Preparing'), ('Awaiting Delivery'), ('Out for Delivery'), ('Delivered')]
        self.cursor.executemany(sql, val)
            
        # #orders inserting
        data3 = pd.read_csv ('file_content/orders.csv')
        df3 = pd.DataFrame(data3)
        for row in df3.itertuples():
            sql = """
            INSERT INTO orders (
                CUSTOMER_NAME,
                CUSTOMER_ADDRESS,
                CUSTOMER_PHONE,
                COURIER_ID,
                ORDER_STATUS_ID,
                PRODUCT_ITEMS) 
                VALUES (%s,%s,%s,%s,%s,%s)
            """ 
            val = (row.CUSTOMER_NAME, row.CUSTOMER_ADDRESS, row.CUSTOMER_PHONE, row.COURIER_ID, row.ORDER_STATUS_ID, row.PRODUCT_ITEMS)
            self.cursor.execute(sql, val)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print(self.cursor.rowcount, "record inserted.")
        
tables = Database()
tables.create_tables()
tables.insert_into_table()

