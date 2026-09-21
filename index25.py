import mysql.connector
try: 
    conn = mysql.connector.connect( 
        host="localhost", user="root", 
        password="kl01cx1870!", 
        database="shop_db" ) 
except mysql.connector.Error as err: 
    print(f"Error: {err}")


cursor = conn.cursor()
cursor.execute( 
    "CREATE TABLE IF NOT EXISTS products (" 
    "id INT AUTO_INCREMENT PRIMARY KEY," 
    "product_name VARCHAR(100)," 
    "price FLOAT,"
    "quantity INT" 
    ")" 
    )


# sql = "INSERT INTO products (product_name,price,quantity) VALUES (%s, %s,%s)" 
# values = ("Mouse",800,20) 
# try: 
#     cursor.execute(sql, values) 
#     conn.commit() 
# except mysql.connector.Error: 
#     conn.rollback()

# cursor.execute("SELECT * FROM products") 
# rows = cursor.fetchall() 
# for row in rows: 
#     print(row) 
# cursor.close()


# sql = "DELETE FROM products WHERE id = %s" 
# values = (5,) 
# cursor.execute(sql, values) 
# conn.commit()


sql = "UPDATE products SET price = %s,WHERE product_name = %s" 
values = (1000,"Laptop")
cursor.execute(sql, values) 
conn.commit()

