import pandas as pd
import pymysql
import os
from dotenv import load_dotenv

# Import CSV
#products
data = pd.read_csv ('file_content/product.csv')   
df = pd.DataFrame(data)
print(df)

#courier
data = pd.read_csv ('file_content/courier.csv')
df = pd.DataFrame(data)
print(df)

#orders
data = pd.read_csv ('file_content/orders.csv')
df = pd.DataFrame(data)
print(df)

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Connect to MYSQL Server
connection = pymysql.connect( 
    host, 
    user, 
    password, 
    database
    )
# cursor object
cursor = connection.cursor()

# Create Table
# product table
sql_query = "CREATE TABLE products (PRODUCT_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, PRODUCT_NAME NVARCHAR(50),PRICE DECIMAL(6,2))"
cursor.execute(sql_query)

#courier table
sql_query = "CREATE TABLE couriers (COURIER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, COURIER_NAME NVARCHAR(50), PHONE_NUM NVARCHAR(50))"
cursor.execute(sql_query)


# Insert DataFrame to Table
#product inserting
for row in df.itertuples():
    sql = "INSERT INTO products (PRODUCT_ID, PRODUCT_NAME, PRICE) VALUES (%s,%s,%s)" 
    val = (row.PRODUCT_ID, row.PRODUCT_NAME, row.PRICE)
    cursor.execute(sql, val)

#courier inserting
for row in df.itertuples():
    sql = "INSERT INTO couriers (COURIER_NAME, PHONE_NUM) VALUES (%s,%s)" 
    val = (row.COURIER_NAME, row.PHONE_NUM)
    cursor.execute(sql, val)
    
#orders inserting 
for row in df.itertuples():
    sql = "INSERT INTO orders (CUSTOMER_NAME,CUSTOMER_ADDRESS,CUSTOMER_PHONE,COURIER_ID,ORDER_STATUS_ID,PRODUCT_ITEMS) VALUES (%s,%s,%s,%s,%s,%s)" 
    val = (row.CUSTOMER_NAME, row.CUSTOMER_ADDRESS, row.CUSTOMER_PHONE, row.COURIER_ID, row.ORDER_STATUS_ID, row.PRODUCT_ITEMS)
    cursor.execute(sql, val)


connection.commit()
print(cursor.rowcount, "record inserted.")
cursor.close()
connection.close()