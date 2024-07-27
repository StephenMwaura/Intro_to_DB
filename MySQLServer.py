import mysql.connector
import getpass
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = getpass.getpass("Enter password: ")

)
mycursor = mydb.cursor()
try:
 query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
 mycursor.execute(query)
 print("Database alx_book_store created successfully!")
except ConnectionError:
 print("Failed to connect to alx_book_store")

mydb.close()