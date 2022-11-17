## REPASO AL COMPORTAMIENTO DE LAS FUNCIONES

e = 'e' # Variable global

def funcion_principal():
    a = 'a' # Variables locales
    b = 'b'
    
    def funcion_anidada():
        c = 'c' # Variables locales
        # Si queremos modificar una variable con un scope diferente
        # a un nivel superior 
        '''
        nonlocal b
        '''
        
        b = 'Cambio de valor'
        print(a)
        print(b)
        # Ambas son creadas en scopes diferentes
        print(id(b))

    funcion_anidada()    
    #print(c) ERROR
    print(id(b))

funcion_principal()


# Retorno de funciones

# Retornamos una función anidada
def saludar():

    def mostrar_mensaje():
        print('Hola!')

    return mostrar_mensaje

respuesta = saludar()

respuesta()

################################
## CLOSURES
################################

def saludar(username):
    mensaje = f'Hola {username}' # Variable Local
    def mostrar_mensaje() : # Anidada
        print(mensaje)
    return mostrar_mensaje

username = 'Jorge'
respuesta = saludar(username)

username = 'a'
# Se usa la variable local cuando la función saludar ya finalizó
# La función mostrar_mensaje tiene memoria
respuesta()


# 