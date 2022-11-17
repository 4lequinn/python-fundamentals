# 1. 
generic_list = list()

# 2. 
generic_list = []


# Pueden almacenar varios tipos de datos
generic_list = [1,True,'uwu']

print(generic_list)

courses_list = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

# Ultimo item
courses_list[-1]

# Actualizar un item
courses_list[4] = 'Rust'

# Sublistas
# [start:end]
# [start:] -> obtenemos los últimos elementos de una lista
# [:end] -> Obtenemos los primeros elementos de la lista
# [start:end:skip]
sub_list = courses_list[0:3]


sub_list = courses_list[::3]

# Agregar elementos a una lista
courses_list.append('MongoDB')
courses_list.append('C#')

len(courses_list)

# index, value
courses_list.insert(1,'Rails')

courses_list2 = ['C','C++','Docker']

# Agregamos los elementos de la 2da lista a la primera sin afectar a la 2da
courses_list.extend(courses_list2)

# Elimina elementos según su valor
courses_list.remove('MongoDB')

# Eliminar según indice
del courses_list[0]

# Vacíar la lista
courses_list.clear()


## Métodos de listas

number_list = list()
# Ordena la lista de menor a mayor por defecto
number_list.sort(reverse=True)

# Número menor y numero mayor
# Ordenamos ascendentemente
number_list.sort()
# Numero menor
number_list[0]
# Numero mayor
number_list[-1]

## Otra forma min - max
# Numero menor
min(number_list)
# Numero mayor
max(number_list)

# Saber si 10 se encuentra en la lista
# Retorna un Bool
10 in number_list

# Me muestra el indice donde se encuentra ese elemento
# Retorna la primera incidencia
index = number_list.index(5)




