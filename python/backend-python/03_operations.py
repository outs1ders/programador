# union de conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)
print(set_c)

# union con operador (|)
print(set_a | set_b)

# interseccion de conjuntos
set_c = set_a.intersection(set_b)
print(set_c)

# intersccion con operador (&)
print(set_a & set_b)

# diferencia de conjuntos
set_c = set_a.difference(set_b)
print(set_c)

# diferencia con operador
print(set_a - set_b)

# diferencia-simetrica de conjuntos
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# diferencia con operador
print(set_a ^ set_b)
