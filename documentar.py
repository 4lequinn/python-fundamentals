# Docstring

# __doc__ (Módulos, Clases, Métodos y Funciones)

# Por convención es como triple comillas dobles y al inicio de la función
def suma(num1, num2):
    """
    La función suma 2 números enteros.

    Argumentos:
    num1: (int)
    num2: (int)

    se retorna la suma de 2 números.

    TODO: 
        *

    >>> suma(10,20)
    30

    """
    return num1 + num2


print(suma.__doc__)

print(help(suma))


# Se puede testear con la doc
# Con el comando python -m doctest <file>.py