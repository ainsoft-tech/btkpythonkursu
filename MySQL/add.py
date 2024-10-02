import mysql.connector

def insertProduct(name, price, imageurl, description):
    connection = mysql.connector.connect(host ="localhost", user = "root", passwd = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name, price, imageurl, description) VALUES (%s, %s, %s, %s)"
    values = (name, price, imageurl, description)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} kayıt eklendi')
        print(f'Son eklenen kaydın Id numarası : {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("Failed inserting into Products {}".format(err))
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host ="localhost", user = "root", passwd = "mysql1234", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name, price, imageurl, description) VALUES (%s, %s, %s, %s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} kayıt eklendi')
        print(f'Son eklenen kaydın Id numarası : {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("Failed inserting into Products {}".format(err))
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapandı.")

list = []
while True:
    name = input('Ürün Adı : ')
    price= float(input('Ürün Fiyatı : '))
    imageurl = input('Ürün Resmi URL : ')
    description = input('Açıklama : ')

    list.append((name, price, imageurl, description))

    result = input('Kayıt ekleme devam edecek misiniz? (e/h)')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor.')
        print(list)
        insertProducts(list)
        break

# insertProduct(name, price, imageurl, description)