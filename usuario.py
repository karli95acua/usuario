class Usuario: #aqui va la clase de mi objeto
    def __init__(self, name, email, saldo, banco): #este es mi constructor
        self.name = name
        self.email = email
        self.balance_cuenta = saldo
        self.banco = banco
    
    #Aqui voy a definir las acciones:
    #Primera acción: hacer un retiro de la cuenta
    def hacer_retiro (self, amount):
        print(f"El usuario {self.name} ha realizado un retiro de {amount} dólares:")
        print(f"Saldo anterior: {self.balance_cuenta} dólares")
        self.balance_cuenta -= amount
        print(f"Saldo actual: {self.balance_cuenta} dólares")
    
    #Segunda acción: mostrar balance usuario
    def mostrar_balance_usuario (self):
        print(f"Balance: El usuario {self.name} tiene un saldo actual de {self.balance_cuenta} dólares, en la institución {self.banco}")
    
    #Tercera acción: hago un deposito
    def hacer_deposito (self, amount):
        print(f"El usuario {self.name} ha realizado un depósito de {amount} dólares:")
        print(f"Saldo anterior: {self.balance_cuenta} dólares")
        self.balance_cuenta += amount
        print(f"Saldo actual: {self.balance_cuenta} dólares")

    #Cuarta acción: transfiero dinero
    def transfer_dinero(self, other_user, amount):
        if self.balance_cuenta - amount < 0:
            print(f"El usuario {self.name} tiene un saldo insuficiente para transferir")
        else:
            self.balance_cuenta -= amount
            other_user.balance_cuenta += amount
            print(f"El usuario {self.name} ha realizado una transferencia por {amount} dólares, a la cuenta de {other_user.name}")
            print(f"El usuario {other_user.name} ha recibido en su cuenta una transferencia de {self.name}, por {amount} dólares")


        
        

#Aqui creo a mis usuarios
usuario_uno = Usuario("Karli Acuña", "karli.am@gmail.com", 120, "Banco Ninja")
usuario_dos = Usuario("Nicolás Gutiérrez", "nicomg@gmail.com", 300, "Banco Nacional")
usuario_tres = Usuario("Ruth Main", "ruthm@gmail.com", 1200, "Banco Ninja")


#Aqui probé que imprima correctamente, antes de probar las acciones
#print(usuario_uno)
#print(usuario_uno.name, usuario_uno.balance_cuenta, usuario_uno.banco)

#Ahora imprimo las acciones que definí
#Que el primer usuario haga 3 depósitos y 1 giro y luego muestre sus balances:
usuario_uno.hacer_deposito(20)
usuario_uno.hacer_deposito(35)
usuario_uno.hacer_deposito(15)
usuario_uno.hacer_retiro(100)
usuario_uno.mostrar_balance_usuario()

#Que el segundo usuario haga 2 depósitos y 2 giros y luego muestre sus balances:
usuario_dos.hacer_deposito(40)
usuario_dos.hacer_deposito(65)
usuario_dos.hacer_retiro(70)
usuario_dos.hacer_retiro(28)
usuario_dos.mostrar_balance_usuario()

#Que el tercer usuario haga 1 depósito y 3 giros y luego muestre sus balances:
usuario_tres.hacer_deposito(36)
usuario_tres.hacer_retiro(50)
usuario_tres.hacer_retiro(6)
usuario_tres.hacer_retiro(10)
usuario_tres.mostrar_balance_usuario()

#Que el primer usuario haga transferencia al tercer usuario y luego muestren sus balances
usuario_uno.transfer_dinero(usuario_tres,90)
usuario_uno.mostrar_balance_usuario()
usuario_tres.mostrar_balance_usuario()

