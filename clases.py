class Usuario:
    pass

mona_xina = Usuario()
print(mona_xina)

# attrs de clase
# attrs de instancia

class User:
    # Atributo de clase
    username = 'Username por default'
    email = ''

print(User.username)


# Atributos de instancia
user1 = User()
# 1. Verifica si el attr existe dentro del objeto
# 2. Verifica si el attr existe dentro de la clase -> lectura
# 3. Lanzar un error 
print(user1.username)


# Ambos attr son lo mismo
print(id(User.username))
print(id(user1.username))

# Meta atributo
# __dict__
print(user1.__dict__)

# Añadimos un attr al objeto
# Atributo de instancia
user1.username = 'x4leqxinn'

# Añado attr dinámicamente
user1.password = '1234'


print(user1.__dict__)



###########################################
## Estandarizar attr para los objetos
###########################################


class UsuarioEstandar:

    def inicializar(self, username, password):
        # Attrs se añaden al objeto
        self.username = username
        self.password = password

user1 = UsuarioEstandar()
user2 = UsuarioEstandar()

user1.inicializar('User1', 'Password1')
user2.inicializar('User2', 'Pass2')

print(user1.__dict__)
print(user2.__dict__)


###########################
## Método __init__
###########################

# Permite inicializar attrs de un objeto al instanciarlo
class UsuarioEstandar:

    # Object
    def __init__(self, username='', password=''):
        # Attrs se añaden al objeto
        self.username = username
        self.password = password

user1 = UsuarioEstandar('user1','pass1')
user2 = UsuarioEstandar('user2','pass2')

print(user1.__dict__)
print(user2.__dict__)