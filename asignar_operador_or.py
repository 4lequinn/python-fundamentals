
# Lectura de izq a derecha
# Se le asigna a la variable el primer valor verdadero
# Es una cualidad del operador or
variable = '' or 'Jorge'
print(variable)

variable = '' or 0 or [] or True
print(variable)


# Una forma de validar esto
listado = [1]
nombre = 'Mona xina'
if listado:
    variable = listado
else:
    variable = nombre
print(variable)

# Mejor forma de validar
listado = [1]
nombre = 'Mona xina'
variable = listado or nombre
print(variable)


