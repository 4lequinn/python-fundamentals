# Métodos de strings más utilizados

# Split
lenguajes = 'Python Ruby Java Rust C++ C'
listado_lenguajes = lenguajes.split() # Por defecto divide el texto por los espacios
print(listado_lenguajes)

# Split -
lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-') # Dividir por -
print(listado_lenguajes)

# Split -
lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-',2) # Dividir por - pero sólo 2 veces
print(listado_lenguajes)


## Crear string apartir de una lista
lenguajes = ['Python', 'Java', 'Ruby', 'Rust']

string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)



