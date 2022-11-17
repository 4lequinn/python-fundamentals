# No se rigen por la regla de los indices
# Se establecen por llaves

generic_dict = {}
generic_dict = dict()
generic_dict = {'Matías':1, 'Jorge':2}

# Valores del diccionario
generic_dict.values()

# Claves del diccionario
generic_dict.keys()

for key, value in generic_dict.items():
    print(key,value)

# Evitamos el error al intentar obtener una clave no existente
user = {
    'name' : 'Jorge',
    'age' : 22,
    'job' : 'developer'
}

skills = user.get('skills', [])
if skills:
    for skill in skills:
        print(skill)


# Enumerar
usuarios = [ 'Eduardo' , ' Fernando ' , ' Uriel' , ' Rafael']
diccionario = { usuario:position + 1
                        for position, usuario in enumerate(usuarios) }
print(diccionario)


# Si se repite una clave, se actualiza con el ultimo valor
# Las llaves se ordenan por orden de declaración

elementos = {'a' : 1, 'b' : 2, 'c':3, 'a': 4}
'''
    elementos['nombre' ] ='Cody' # Crea la llave con su valor
    elementos[(1, 2, 3)] =' La llave es una tupla'
    # Actualiza el valor de la llave
    elementos['nombre'] = ' mona xina'
'''
print(elementos)
print(len(elementos))

