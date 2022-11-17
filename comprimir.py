generic_list = [1,2,3,4,5]

generic_tuple = (10,20,30,40,50)

result = zip(generic_list, generic_tuple) # -> zip

# Objeto de tipo de dato zip
print(result)

# Me permite combinar tuplas y listas
result = tuple(result)

# Si sobran valores, los restantes serán omitidos

