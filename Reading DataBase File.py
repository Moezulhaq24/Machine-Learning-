import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "*****", # Use your password here
    database = "company"
)

if mydb.is_connected():
    print("Connection is Successfull")

else:
    print("Could'nt Connected")

