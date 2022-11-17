
# Declaramos las variables
one, two, three, four = 1,2,3,4


# Se pueden asignar con una tupla
numbers = (1,2,3,4)
one, two, three, four = numbers


# Prefijo *
# Asterísco denota lista
# * -> lista

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *resto_valores = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
# Me crea una lista con el resto de valores
print(resto_valores)



# En el caso de que no quieras guardar los valores
# utilizamos el * y un underscore para decirle a python que no queremos trabajar lo que siga
# _ -> Omitir valor
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_ = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

# Omitimos los valores entre el 4 y 9
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)


# Mostramos en una lista los valores que no desempaquetamos
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *resto_numeros, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

# Excluir numeros
# _ -> Omite
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
