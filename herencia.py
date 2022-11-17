class Mascota: # Clase padre
    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')

class Perro(Mascota): # Clase hija
    pass

bichoto = Perro()

bichoto.dormir()



############################################
# Python permite herencia Múltiple
############################################

class Felino:
    def cazar(self):
        print('Felino caza')

class Gato(Mascota, Felino):
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Sobrescribir un método    
    def comer(self):
        # Nos permite acceder al padre inmediato de la clase
        super().comer()
        print(f'{self.nombre} come.')



neko = Gato('Kawai')
neko.cazar()
neko.comer()

# Primero busca en Gato, si no existe el método sube un nivel jerarquico


##############################
## Métodos de clase 
##############################

class Circulo:
    
    pi = 3.141592

    # cls hace referencia a la clase por convención
    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)