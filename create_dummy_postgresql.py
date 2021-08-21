import psycopg2
import pandas as pd

data = pd.read_csv("Product_data.csv")
dataframe = pd.DataFrame(data)

connection = psycopg2.connect(
    host="localhost",
    database="BusinessBuddy",
    user="postgres",
    password="admin"
)

cursor = connection.cursor()

for index, row in dataframe.iterrows():
    print(row)
    print("_________")
    cursor.execute(f"""
    INSERT INTO fb_app_product(product_title,product_description, listing_unit_price,created_at,updated_at) 
    VALUES('{row['product_title']}', '{row['product_description']}', '{row['listing_unit_price']}', '{row['created_at']}', '{row['updated_at']}');
    """)

connection.commit()
connection.close()