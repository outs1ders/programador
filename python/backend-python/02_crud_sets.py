set_countries = {'col', 'mex', 'bol'}

# Cantidad de elementos
size = len(set_countries)
print(size)

# Elementos dentro del conjunto
print('col' in set_countries)
print('per' in set_countries)

# agregar (add)
set_countries.add('per')
print(set_countries)

# No se repite por mas que se agregue varias veces
set_countries.add('per')
print(set_countries)

# actulizar (update)
set_countries.update({'ar', 'ecua', 'per'})
print(set_countries)

# Eliminar (remove)
set_countries.remove('col')
print(set_countries)

# Eliminar un elemento si tal vez no existe
set_countries.discard('arg')
print(set_countries)

# Eliminar todo el conjunto
set_countries.clear()
print(set_countries)
