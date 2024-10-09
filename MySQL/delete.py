import mysql.connector

def deleteProduct():
    connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node-app")
    cursor = connection.cursor()

    sql = "delete from products where id=%s"
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt silindi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

deleteProduct(4)