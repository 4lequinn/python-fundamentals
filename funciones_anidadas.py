
# 1.
def operacion():
    
    def deposito(cantidad, balance):
        return cantidad + balance
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    print(deposito(10, 20))
    print(retiro(50, 30))

    
operacion()


# 2.
def operacion(cantidad, balance, tipo='deposito'):
    
    def deposito(cantidad, balance):
        return cantidad + balance
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad,balance)


print(operacion(10,30))
