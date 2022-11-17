# Se parecen a las listas
# La pricipal diferencia es que las tuplas son inmutables

generic_tuple = ()
print(generic_tuple)

generic_tuple2 = (1,True,'uwu', [], ())

cursos = ('Python' , ' Flask' , 'Django' , 'Rails' , 'MongoDB')
# 0 1 2 3 4

primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

# Toma todos los elementos de la tupla original
sub_tupla = cursos[:]
print(sub_tupla)


## Conversión tuplas y listas

cursos = ['Python' , ' Django' , ' Flask']
cursos_tupla = tuple(cursos)

print(cursos_tupla)
print(type(cursos_tupla))

niveles = ('Básico' , 'Intermedio' , 'Avanzado')
niveles_lista = list(niveles)

print(niveles_lista)
print(type(niveles_lista))
