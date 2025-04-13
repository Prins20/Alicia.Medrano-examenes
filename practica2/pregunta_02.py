"""Usando el concepto de herencia y encapsulación (para el atributo saldo)
para crear el siguiente programa (3 ptos):
Reglas: - Crear una clase llamada Persona y agregar un atributo saldo a esta clase
(ejercicio anterior). - Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada - El método transferencia hace que la clase
Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en
su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando
una transferencia y con dos personas."""



class Persona:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self._saldo = saldo

    def mostrar_saldo(self):
        print(f"Saldo de {self.nombre}: {self._saldo}")

   
    def transferencia(self, monto, persona_destino):
        
        if self._saldo >= monto:
            self._saldo -= monto
            persona_destino._saldo += monto
            print(f"Transferencia exitosa de {monto} de {self.nombre} a {persona_destino.nombre}")
        else:
            print(f"Saldo insuficiente para realizar la transferencia.")


<<<<<<< HEAD

=======
>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
class Empleado(Persona):
    def __init__(self, nombre, saldo, edad, nacionalidad="peruana"):
        super().__init__(nombre, saldo)
        self.edad = edad
        self.nacionalidad = nacionalidad

<<<<<<< HEAD

=======
>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
    def cumpleaños(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.nombre}, ahora tiene {self.edad} años.")

<<<<<<< HEAD

=======
>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
    def aumento_sueldo(self):
        self._saldo *= 1.30
        print(f"El sueldo de {self.nombre} después de un aumento del 30% es: {self._saldo}")

<<<<<<< HEAD

=======
>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
    def mensaje_edad(self, año):
        edad_en_año = self.edad + (año - 2025)
        print(f"En el año {año} {self.nombre} tendrá {edad_en_año} años.")


<<<<<<< HEAD

=======
>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
empleado1 = Empleado("Carlos Pérez", 5000, 30)
empleado2 = Empleado("Ana García", 3000, 25)

empleado1.mostrar_saldo()
empleado2.mostrar_saldo()

empleado1.transferencia(2000, empleado2)

empleado1.mostrar_saldo()
empleado2.mostrar_saldo()
<<<<<<< HEAD

=======
>>>>>>> 4ff1a8a03bc8acacd3b40918fa56ee0ecbdff02d
empleado1.transferencia(3500, empleado2)
