import mysql.connector
connection= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "schooldb"
)

# mycursor = connection.cursor()

# mycursor.execute("CREATE DATABASE IF NOT EXISTS <databasename>>")
# mycursor.execute("create table <tablename> (name varchar(255), address varchar(255))")

# print(connection)

"""
Veritabanlarını göstermek için 

mycursor = connection.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)
"""