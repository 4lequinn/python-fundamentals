
# Función vacía
def suma():
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    result = num1 + num2
    print(result)

sum()


# Parámetros o argumentos (hacen a la función mas abstracta)
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

def suma(num1, num2):
    result = num1 + num2
    print(result)

sum(num1, num2)

# Retornar valores
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

def suma(num1, num2):
    return num1 + num2, 'Retorno de un texto' #, n cantidad de valores

result, _ = sum(num1, num2)


# Valores por default
# se deben poner parametros con valores por default siempre a la derecha
def area_circulo(radio, pi = 3.14):
    return pi * (radio ** 2)

# Los parametros se pueden trabajar y referenciar con nombres
resultado = area_circulo(radio=10, pi=3.141592)
print(resultado)

################################################
## Argumentos Args
################################################

# La función print puede recibir n cant de argumentos, no está limitada.
print('String', True, 1)

# Entregando un argumento de tipo lista
def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10,10,5,7,10])
print(resultado)

# Entregando varios argumentos
# Por convención todos aquellos parametros que tengan asterisco deben llamarse args
def promedio(*args): # -> tuple
    print(type(args))
    return sum(args) / len(args)

resultado = promedio(10,10,5,7,10)
print(resultado)

# Se pueden asignar más parametros en conjunto con args
def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1 , 8, 8, p4 = 1000)



#######################################
## kwargs
#######################################

# Diccionarios

def usuarios(**kwargs): # -> Dict
    print(kwargs)
    print(type(kwargs))

# Los nombre son usados como llaves
# Por convención los el valor de los parametros debe estar todo junto, sin espacios
usuarios(eduardo=[10,10,8], fernando=[10,9,8])

## Se pueden usar args y kwargs
def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')


