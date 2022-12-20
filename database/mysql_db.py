import connect_db as db

class Database():
    def __init__(self) -> None:
        pass
    
    def create_tables(self):
        self.create_product_tables()
        self.create_courier_table()
        self.create_status_table()
        self.create_orders_table()
        db.connection.commit()
        db.cursor.close()
        db.connection.close()
        print("Tables Created")

    def create_product_tables(self):
        product_table = """
            CREATE TABLE if not exists products (
                PRODUCT_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                PRODUCT_NAME NVARCHAR(50),
                PRICE DECIMAL(6,2)) """
        db.cursor.execute(product_table)

    def create_courier_table(self):
        courier_table = """
            CREATE TABLE if not exists couriers (
                COURIER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                COURIER_NAME NVARCHAR(50),
                PHONE_NUM NVARCHAR(50))"""
        db.cursor.execute(courier_table)

    def create_status_table(self):
        order_staus_table = """
            CREATE TABLE if not exists order_status (
                ORDER_STATUS_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                ORDER_STATUS NVARCHAR(50))"""
        db.cursor.execute(order_staus_table)

    def create_orders_table(self):   
        orders_table = """
            CREATE TABLE if not exists orders (
                ORDER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
                CUSTOMER_NAME NVARCHAR(50), CUSTOMER_ADDRESS NVARCHAR(250), 
                CUSTOMER_PHONE NVARCHAR(50), COURIER_ID INT NOT NULL, 
                ORDER_STATUS_ID INT NOT NULL, PRODUCT_ITEMS CHAR(50), 
                FOREIGN KEY (COURIER_ID) REFERENCES couriers(COURIER_ID) 
                    ON DELETE CASCADE, 
                FOREIGN KEY (ORDER_STATUS_ID) REFERENCES order_status(ORDER_STATUS_ID) 
                    ON DELETE CASCADE)"""
        db.cursor.execute(orders_table)

if __name__ == "__main__":
    tables = Database()
    tables.create_tables()