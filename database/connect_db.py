import pymysql
import os
from dotenv import load_dotenv

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
print('Database Connected')
