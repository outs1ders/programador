# Definir un conjunto (set)
set_countries = {'col', 'mex', 'bol'}

print(set_countries)
print(type(set_countries))

# El conjunto no puede repetir elementos
set_numbers = {1, 2, 2, 3, 454, 12}
print(set_numbers)

# El conjunto resive todo tipo de datos
set_types = {1, 'dia', False, 12.42}
print(set_types)

# Definir un conjunto apartir de una string
set_from_string = set('hoola')
print(set_from_string)

# Definir un conjunto apartir de una tupla
set_from_tuples = set(('abc', 'cde', 'efg'))
print(set_from_tuples)

# Definir un conjunto apartir de una lista
numbers = [1, 2, 3, 1, 2, 3, 4, 5]
set_numbers = set(numbers)
print(set_numbers)

#transformar de un conjunto a una lista
unique_numbers = list(set_numbers)
print(unique_numbers)