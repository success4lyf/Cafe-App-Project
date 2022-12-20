import pandas as pd
import connect_db as db

class Insert():
    def __init__(self) -> None:
         pass

    def insert_into_tables(self):
        self.insert_into_products()
        self.insert_into_couriers()
        self.insert_into_status()
        self.insert_into_orders()
        db.connection.commit()
        db.cursor.close()
        db.connection.close()
        print(db.cursor.rowcount, "record inserted.")

    def insert_into_products(self):
        data1= pd.read_csv ('file_content/product.csv')   
        df1 = pd.DataFrame(data1)
        for row in df1.itertuples():
            sql = "INSERT INTO products (PRODUCT_NAME, PRICE) VALUES (%s,%s)" 
            val = (row.PRODUCT_NAME, row.PRICE)
            db.cursor.execute(sql, val)
    
    def insert_into_couriers(self):
        data2 = pd.read_csv ('file_content/courier.csv')
        df2 = pd.DataFrame(data2)
        for row in df2.itertuples():
            sql = "INSERT INTO couriers (COURIER_NAME, PHONE_NUM) VALUES (%s,%s)" 
            val = (row.COURIER_NAME, row.PHONE_NUM)
            db.cursor.execute(sql, val)

    def insert_into_status(self):
        sql = "INSERT INTO order_status (ORDER_STATUS) VALUES (%s)"
        val = [('Preparing'), ('Awaiting Delivery'), ('Out for Delivery'), ('Delivered')]
        db.cursor.executemany(sql, val)

    def insert_into_orders(self):
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
            db.cursor.execute(sql, val)

if __name__ == "__main__":
    tables = Insert()
    tables.insert_into_tables()

