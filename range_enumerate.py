# Función Range

rango = range(11) # 0 - 10

for valor in rango:
    print(valor)

# start = 0:end: skips
for x in range(0,21,2):
    print(x)


# Función Enumerate
numeros = [10,20,30,40,50]

# collection:start
for i, num in enumerate(numeros):
    print(i,num)