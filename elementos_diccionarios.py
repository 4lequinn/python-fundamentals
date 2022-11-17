diccionario = {'a':1,'b':2,'c':3}

valor = diccionario['c']
print(valor)

# Retorna falso
print('z' in diccionario)

# get 
# Retorna None si no se encuentra
# se encuentra implicito el valor None por default
value = diccionario.get('z', None)
print(value)

# setDefault
# Si la llave no existe se añade
value = diccionario.setdefault('e',5)
print(value)


# Llaves 
keys = tuple(diccionario.keys())

# Valores
values = tuple(diccionario.values()) 

# Elementos
items = tuple(diccionario.items())


# Eliminar un elemento por una llave
del diccionario['a'] #1

# Retorna el valor de la llave
value = diccionario.pop('b') #2

# Elimina todos los elementos
diccionario.clear #3