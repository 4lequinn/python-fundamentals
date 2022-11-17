# Scope

# las 2 variables "animal" son diferentes
# tienen alcances diferentes

# Variable Global
animal = 'León'

def imprimir_animal():
    # Variable Local
    animal = 'Ballena'

    # Si queremos utilizar la variable global debemos especificar
    # global animal
    
    print(animal)
    # Identificador de la variable
    print(id(animal))

imprimir_animal()

print(animal)
# Son objetos diferentes
print(id(animal))

