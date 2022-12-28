import mysql.connector

def createDB():
    db = mysql.connector.connect(
    host='localhost',
    user='outs',
    password='Adminishere1')

    namedb = input("Nombre de la base datos que desea crear: ")
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE {}".format(namedb))

    except:
        print('La base de datos {} ya existe'.format(namedb))
        createDB()


def menu():
    print(
        """
        1| Crear una base de datos
        2| 
        3|


        """
    )


if __name__ == '__main__':

    createDB()