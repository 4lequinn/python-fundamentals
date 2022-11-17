
# Ejemplo sabiendo la cant de iteraciones
contador = 1
while contador <= 10:
    print(contador)
contador = contador + 1


# Se ocupa siempre y cuando no se sabe la cantidad de iteraciones que vamos a realizar
# Su mejor uso

# Bloque else (opcional) debido a que while evalua una condicion
numero = 123456789
contador_digitos = 0
while numero >= 1:
    #contador_digitos = contador_digitos + 1
    # abreviatura
    contador_digitos += 1
    numero = numero / 10 
else:
    print(contador_digitos)
    print('Fin de el ciclo while')

