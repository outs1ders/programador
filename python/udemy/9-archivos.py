# open files
#c = open('lol.txt') #se llama al archivo por su nombre y se le pueden dar mas parametross

# c = open('example',|r| or |a| or |w| or |x|) ---

#   r = read    "se utiliza para leer el archivo ya credo"
#   a=append    "se utiliza para abrir y modificar el archo sin alteral el contenido original"
#   w=write     "se utiliza para modificar cualquier parte del archivo o crearlo si este no exite,pero este mismo
#                borra a su vez el contenido que alla en el archivo"
#   x=create    "se usa ara crear el archiv si este no existe"


# "print(c.read())" --- # se utiliza para leer el archivo por terminal

# "print(c.readline())" --- # se utiliza para leer un  archivo linea por linea

# "for x in c:  --- #se utilixa para manipular cada linea de forma independiente
#    print(x)"

# "c.close()" --- #se utliza para cerrar el archivo

"""
c=open('lol.txt', 'a')
c.write('\nagrega otra linea de texto')

c.close

"""

# borar un archivo
import os   #se hace por medio de la libreria os

# "os.remove('lol.txt')"    # "os.remove('file')" lo utilizamos para borrar el archivo en cuestion

# comprovar si el archivo existe
if os.path.exists('lol.txt'):   # "os.path.exists('file')" lo utilizamos para revisar si el archivo existe
    os.remove('lol.txt')
else:
    print('el archivo no existe')

#borar una carpeta
os.rmdir('mi_carpeta')  # "os.rmdir('folder')" lo utiizamos para borrar una capeta