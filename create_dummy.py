## This code to create dummy data in the Customers Table

# import pandas as pd
# import sqlite3

# data = pd.read_csv("Customer_data.csv")
# df = pd.DataFrame(data)



# connect = sqlite3.connect("db.sqlite3")
# cursor = connect.cursor()
# for index, row in df.iterrows():
#     # main_id,first_name,last_name,email,gender,age,mobile_no_1,mobile_no_2,mobile_no_3,city,state,country,address,profession,customer_source,description,additional_notes,bank_details,time_zone,created_at,updated_at
#     # print(row['main_id'], row['first_name'], row['last_name'], row['email'], row['gender'], row['age'], row['mobile_no_1'], row['mobile_no_2'], row['mobile_no_3'], row['city'], row['state'], row['country'], row['address'], row['profession'], row['customer_source'], row['description'], row['additional_notes'], row['bank_details'], row['time_zone'], row['created_at'], row['updated_at'])
#     cursor.execute(f"""
#     INSERT INTO fb_app_customer(first_name,last_name,email,gender,age,mobile_no_1,mobile_no_2,mobile_no_3,city,state,country,address,profession,customer_source,description,additional_notes,bank_details,time_zone,created_at,updated_at) VALUES("{row['first_name']}", "{row['last_name']}", "{row['email']}", "{row['gender']}", "{row['age']}", "{row['mobile_no_1']}", "{row['mobile_no_2']}", "{row['mobile_no_3']}", "{row['city']}", "{row['state']}", "{row['country']}", "{row['address']}", "{row['profession']}", "{row['customer_source']}", "{row['description']}", "{row['additional_notes']}", "{row['bank_details']}", "{row['time_zone']}", "{row['created_at']}", "{row['updated_at']}")
#     """)
# print("datainserted")
# connect.commit()
# connect.close()







# This code to create dummy data in the Products Table

import pandas as pd
import sqlite3

data = pd.read_csv("Product_data.csv")
df = pd.DataFrame(data)



connect = sqlite3.connect("db.sqlite3")
cursor = connect.cursor()
for index, row in df.iterrows():
    cursor.execute(f"""
    INSERT INTO fb_app_product(product_title,product_description, listing_unit_price,created_at,updated_at) VALUES("{row['product_title']}", "{row['product_description']}", "{row['listing_unit_price']}", "{row['created_at']}", "{row['updated_at']}")
    """)
print("datainserted")
connect.commit()
connect.close()

