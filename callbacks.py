# Funciones que se usan como argumento para otras funciones

promedio = lambda *args : sum(args) / len(args)

print(promedio(7,7,3,6))

aprobado = lambda calificacion : calificacion >= 4

print(aprobado(2))


## CALLBACK
# Divide y Vencerás!

def mostrar_mensaje(func_promedio, func_aprobado, *args):
    promedio = func_promedio(*args)
    if func_aprobado(promedio):
        print(f'Felicidades! aprobaste con un promedio {promedio}')
    else:
        print('Reprobaste con promedio {}'.format(promedio))


mostrar_mensaje(promedio,aprobado,5,5,5,2)

# Creo otra función para determinar si el alumno aprueba o no
# según otros factores etc
def es_aprobado(calificacion):
    return calificacion >= 7

# No hace falta modificar la función principal
mostrar_mensaje(promedio,es_aprobado,5,5,5,2)

# Callback sirven en sistema modulares
# Donde puedes reemplazar un pieza de software por otra

