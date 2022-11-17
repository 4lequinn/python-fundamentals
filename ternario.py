
# Solución sin ternario
calificacion = 5
color = None
if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'
print(calificacion, color)

# Solución con ternario

calificacion = 5
color = 'Verde' if calificacion >= 7 else 'Rojo'
print(calificacion, color)