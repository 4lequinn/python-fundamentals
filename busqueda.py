course_title = 'Curso profesional de Python'

# Cuenta la cantidad de veces que aparece la palabra python
count  = course_title.count('Python')
print(count)

# Saber si existe un string o no en el string
# Return Bool
print('python' in course_title.lower())

# Saber si comienza con algo
# Return Bool
print(course_title.startswith('Curso'))

# Saber si termina con algo
# Return Bool
print(course_title.endswith('Python'))
