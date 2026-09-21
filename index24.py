import mysql.connector
# conn = mysql.connector.connect( 
#     host="localhost", 
#     user="root", 
#     password="kl01cx1870!", 
#     database="amal" 
#     )
# if conn.is_connected(): 
#     print("Connected successfully!")
try: 
    conn = mysql.connector.connect( 
        host="localhost", user="root", 
        password="kl01cx1870!", 
        database="school_db" ) 
except mysql.connector.Error as err: 
    print(f"Error: {err}")

cursor = conn.cursor()
cursor.execute( 
    "CREATE TABLE IF NOT EXISTS students (" 
    "id INT AUTO_INCREMENT PRIMARY KEY," 
    "name VARCHAR(255)," 
    "age INT" 
    ")" 
    )

# Inserting data
# sql = "INSERT INTO students (name, age) VALUES (%s, %s)" 
# values = ("deepak", 23) 
# try: 
#     cursor.execute(sql, values) 
#     conn.commit() 
# except mysql.connector.Error: 
#     conn.rollback()


# Reading Data
# cursor.execute("SELECT * FROM students") 
# rows = cursor.fetchall() 
# for row in rows: 
#     print(row) 
# cursor.close() 
# conn.close()

# Updating Data
# sql = "UPDATE students SET age = %s WHERE id = %s" 
# values = (21, 1) 
# cursor.execute(sql, values) 
# conn.commit()

# Delete data
# sql = "DELETE FROM students WHERE id = %s" 
# values = (1,) 
# cursor.execute(sql, values) 
# conn.commit()