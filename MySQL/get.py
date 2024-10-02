import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host ="localhost", user = "root", passwd = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products')

    result = cursor.fetchall()

    for product in result:
        print(product)

getProducts()