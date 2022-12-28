"""
#importar   #lo utlizamos para usar codigo de otros archivos
import modulos as xs #utilizamos "as" ara cambiar el nombre al modulo que hemos importado

print(xs.mascotas)
xs.saludo("juan")

#from import
from modulos import saludo, mascotas #utilizamos from para llamar algo especifico en el modulo 

print(mascotas)



from camelcase import CamelCase

c=CamelCase()
s="esta horacion necesita CamelCase"

camelcases=c.hump(s)
print (camelcases)

"""
#comandos de pip

#list  --   se usa para mirar los paquets de pip instalados
#pip list

#unistall   --   se utiliza para desintalar un paquete de pip
#pip unistall