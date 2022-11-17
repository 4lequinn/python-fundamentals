nombre = 'Jorge Alejandro'
apellido = 'Quintui'

# 1.
nombre_completo = 'Mr. ' + nombre + ' ' + apellido + '.'

# 2.
nombre_completo = 'Mr. %s %s.' %(nombre, apellido)

# 3.
nombre_completo = 'Mr. {} {}.'.format(nombre,apellido)

# 4.
nombre_completo = 'Mr. {nombre} {apellido}.'.fomat(
    nombre = nombre,
    apellido = apellido
)

# 5. f string
nombre_completo = f'Mr. {nombre} {apellido} {"Vergara"}'

# Función print (Imprime en consola)
print(nombre, apellido)

print(nombre, apellido, sep='-')

