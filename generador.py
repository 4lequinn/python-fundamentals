# Función que retorna objetos sin que esta finalice

def pares(): # Generador -> Lazy Iterator
    for numero in range(0,12,2):
        #return numero
        yield numero # suspende de forma momentarea la ejecución de la funcion
        print('Se reanuda la ejecución')

# La función se puede reanudar donde se detuvo

# Se ve un objeto de tipo generador
# Podemos obtener sus valores bajo demanda
'''
print(pares())

for par in pares():
    print(par)
'''


# Ayuda en el uso de memoria (Cuando se habla de muchos registros y más rápidos)
"""
generador = pares()

print(next(generador))
print(next(generador))
print(next(generador))

"""

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador Finalizó')
        break


# Permite consumir los datos sin la necesidad de recorrer todos a la vez