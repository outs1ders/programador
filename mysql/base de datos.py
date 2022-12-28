import mysql.connector
import os

DBs = []

def createDB(clave):
    db = mysql.connector.connect(
    host='localhost',
    user='root',
    password= clave
    )

    namedb = input("Nombre de la base datos que desea crear: ")

    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE {}".format(namedb))  
        DBs.append(namedb)

    except:
        print('La base de datos {} ya existe'.format(namedb))
        createDB()


def dbseleccion():
    
    print(' Hola \n tus bases de datos a llenar son: \n')
   
    num = 1

    for i in DBs:
        print("[{}] {}".format(num,i))
        num += 1


    selec = int(input('\nselecciones una: '))
    
    seleccion = selec - 1
    
    return DBs[seleccion]


if __name__ == '__main__':
    

    cantidad = int(input("cuantas bases de datos desea crear: "))
    
    clave = input("ingrese la contraseña del root de su base de datos [localhost] : ")

    for i in range(cantidad):
        createDB(clave)

    os.system("cls")

    while True:

        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password= clave,
            database= dbseleccion()
        )

        cursor = db.cursor()

        os.system("cls")

        tabla = input('ingrese el nombre de la tabla: ')
        num = int(input('Cuantas columnas desea crear: '))

        nombreColumna = []
        tipoDato = [] 

        for i in range(num):
            nombre = input('nombre de la columna  [num. {}] : '.format(i+1))
            nombreColumna.append(nombre)

            dato = input('ingrese el tipo del dato : \n[1] int \n[2] varchar ')

            if dato == '1':
                tipoDato.append('INT')
                os.system('cls')

            elif dato == '2':
                varchar = input('Que tan grande desea el varchar [numero] :')
                tipoDato.append('VARCHAR({})'.format(varchar))
                os.system('cls')

        try:
            cursor.execute("CREATE TABLE {} (id int PRIMARY KEY NOT NULL AUTO_INCREMENT)".format(tabla))
        
            for i in range(num):
                cursor.execute("ALTER TABLE {} ADD {} {}".format(tabla, nombreColumna[i], tipoDato[i]))

        except:
            cursor.execute('SHOW TABLES')
            for x in cursor:
                print (x)

    
        cantidadDatos = int(input('Cuantos datos desea ingresar en la tabla: '))

        columnas = ''
        values = ''
        contador = 0

        for i in nombreColumna:
        
            columnas += i
            values += '%s'
            contador += 1

            if i == nombreColumna[-1]:
                columnas += ''
                values += ''     

            else:
                columnas += ','
                values += ','



        for i in range(cantidadDatos):

            sql = "INSERT INTO {} ({}) values ({}) ".format(tabla, columnas, values)
            valor = []

            for j in range(contador):
            
                informacion = input('ingrese la informacion para la columba de {} : '.format(nombreColumna[j]))
                valor.append(informacion)

                os.system('cls')


            valores = tuple(valor)
            cursor.execute(sql,valores)
            db.commit() 

        
        fin = input('Desea salir ya [s/n]  : ')

        if fin == "s" or fin == "S":
            break



