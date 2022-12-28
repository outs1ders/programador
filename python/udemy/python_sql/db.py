import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='outs1der',
    password='Theadminishere1',
    database='Prueva'
)

cursor=midb.cursor()

#listar datos
cursor.execute('select * from Usuario')
resultado= cursor.fetchall()
# - fetchall = devuelve todos los elementos
# - fetchone = devuelve el primer elemento que halla encontrado
print(resultado)

# -listar datos, limitando la consulta
#cursor.execute('select * from Usuario limit 1') 
# -limit [numero], devuelve la candiad deresultados con el numero ingreado
#resultado= cursor.fetchall()
#print(resultado)

#ver definicion de tablas
#cursor.execute('show create table Usuario')

#insertar datos
#sql = 'insert into Usuario (email, username) values (%s,%s)'
#values = ('micorreo@google.com', 'sironmaster')
#cursor.execute(sql,values)
#midb.commit()
#print(cursor.rowcount)

#actualizar datos
#sql = 'update Usuario set email = %s where id = (%s)'
#values = ('mico@correo.com',4)
#cursor.execute(sql,values)
#midb.commit()

#eliminar datos
#sql = 'delete from Usuario where id = %s'
#values = (4, )
#cursor.execute(sql,values)
#midb.commit()