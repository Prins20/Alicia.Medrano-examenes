"""Escribir un programa para gestionar una billetera electrónica (3 ptos):
Reglas: - El programa deberá considerar 2 cuentas bancarias: 1 en soles y
otra en dólares. Considerar el nombre y apellido del titular - Deberá tener
un método para transferir entre sus cuentas, pero
para realizar esto debe hacer una conversión de monedas. - Tendrá otro
método para retirar dinero, esto debe actualizar ambas
cuentas y mostrar en pantalla los montos actualizados, a su vez
validar si tiene fondos suficientes o no para el retiro, mostrar un
mensaje que indique no tiene suficientes en caso fuera el caso. -
Instanciar 3 veces los casos de transferencias para ver reflejado el
uso de tus métodos creados."""


class BilleteraElectronica:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares, tipo_cambio=3.5):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares
        self.tipo_cambio = tipo_cambio

    def mostrar_saldos(self):
        print(f"Titular: {self.nombre} {self.apellido}")
        print(f"Saldo en Soles: {self.saldo_soles} soles")
        print(f"Saldo en Dólares: {self.saldo_dolares} USD")

    def transferir(self, monto, de_cuenta, a_cuenta):
        if de_cuenta == "soles" and a_cuenta == "dolares":
            if self.saldo_soles >= monto:
                self.saldo_soles -= monto
                self.saldo_dolares += monto / self.tipo_cambio
                print(f"Transferencia de {monto} soles a dólares exitosa.")
            else:
                print(f"No tienes suficientes soles para realizar la transferencia.")

        elif de_cuenta == "dolares" and a_cuenta == "soles":
            if self.saldo_dolares >= monto:
                self.saldo_dolares -= monto
                self.saldo_soles += monto * self.tipo_cambio
                print(f"Transferencia de {monto} dólares a soles exitosa.")
            else:
                print(f"No tienes suficientes dólares para realizar la transferencia.")
        else:
            print("Tipo de transferencia no válido.")

        self.mostrar_saldos()

    def retirar(self, monto, cuenta):
        if cuenta == "soles":
            if self.saldo_soles >= monto:
                self.saldo_soles -= monto
                print(f"Retiro de {monto} soles realizado exitosamente.")
            else:
                print("No tienes suficientes soles para realizar el retiro.")

        elif cuenta == "dolares":
            if self.saldo_dolares >= monto:
                self.saldo_dolares -= monto
                print(f"Retiro de {monto} dólares realizado exitosamente.")
            else:
                print("No tienes suficientes dólares para realizar el retiro.")
        else:
            print("Cuenta no válida para retiro.")

        self.mostrar_saldos()

<<<<<<< HEAD
=======

>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
billetera1 = BilleteraElectronica("Carlos", "Pérez", 5000, 1500)
billetera2 = BilleteraElectronica("Ana", "García", 1000, 2000)
billetera3 = BilleteraElectronica("Luis", "Martínez", 2000, 800)

print("Billetera 1 (Carlos Pérez):")
billetera1.mostrar_saldos()
print("\nBilletera 2 (Ana García):")
billetera2.mostrar_saldos()
print("\nBilletera 3 (Luis Martínez):")
billetera3.mostrar_saldos()

print("\nRealizando transferencias:")
billetera1.transferir(1000, "soles", "dolares")  # De soles a dólares
billetera2.transferir(300, "dolares", "soles")  # De dólares a soles
billetera3.transferir(500, "soles", "dolares")  # De soles a dólares

print("\nRealizando retiros:")
billetera1.retirar(2000, "soles")
billetera2.retirar(1500, "dolares")
billetera3.retirar(1000, "soles")
