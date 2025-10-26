import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost')

    cursor = connection.cursor()
    cursor.execute("Create DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
