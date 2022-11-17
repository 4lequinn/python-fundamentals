# Las funciones son de primer orden
# Pueden ser usadas para:

# 1. Asignar a variables
# 2. Como argumentos a otras funciones
# 3. Funciones pueden retornar funciones


def centigrados_farhenheit(grados):
    return grados * 1.8 + 32

print(centigrados_farhenheit(10))
print(centigrados_farhenheit(-2))

# Funciones lambdas se usan cuando no sabemos cuando requerimos la funcionalidad de la misma
# Guardando la función desde una variable y utilizandola bajo demanda

mi_funcion = centigrados_farhenheit
# Type function
print(type(mi_funcion))

print(mi_funcion(50))


# Funciones lambdas también conocidas como funciones anónimas
# Se expresan en una linea, no poseen nombre, generalmente realizan tareas pequeñas

# Convertimos la función centigrados_farhenheit a funcion lambda
funcion_grados = lambda grados : grados * 1.8 + 32
# lambda <parameters> : <body>
# por defecto la función lambda retorna el valor expresado en el cuerpo de la función
print(funcion_grados(10))

"""
sin_parametros = lambda : True
paremtros_default = lambda p1=10, p2=20 : p1 + p2
asterisco = lambda *args, **kwargs : len(args) + len(kwargs) 
"""

## En el cuerpo siempre debe haber una expresión que se ejecute
# Inclusive si retorna o no



