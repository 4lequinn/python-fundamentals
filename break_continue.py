
## Break permite finalizar cualquier tipo de ciclo
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:
    if caracter == 'P':
        break
print(caracter)

## Continue hará que el ciclo salte a la siguiente iteración
# El código que continua después no se ejecutará
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:
    if caracter == ' ':
        continue
print(caracter)



