import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host ="localhost", user = "root", passwd = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    cursor.execute('SELECT name, price, description FROM products  order By price asc')

    result = cursor.fetchall() #veritabanındaki tüm kayıtlar getirilir.
    # result = cursor.fetchone() #veritanındaki ilk kaydı getirir.

    for product in result:
        print(f'{product[0]} {product[1]}')

getProducts()