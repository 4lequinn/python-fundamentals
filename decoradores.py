# Es una característica de python
# Cuando se habla de decorador 
# se trabaja por lo menos 3 funciones
# Input, Output y la función principal

"""
a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

a(b) -> c
"""

# Podemos extender funcionalidades

# ESTRUCTURA BASE PARA UN DECORADOR
def funcion_a(funcion_b):

    # Función decorada
    def funcion_c(*args, **kwargs):
        print('>> シニガミ')

        resultado = funcion_b(*args, **kwargs)

        print('セメンテリオ <<')
        
        return resultado

    return funcion_c

# Un decorador nos permite ejecutar código antes o después de la función
@funcion_a
def saludar():
    print('Hola, Nos encontramos en una función!')

saludar()


## Decoradores complejos

@funcion_a
def suma(num1, num2):
    return num1 + num2

result = suma(10, 20)




