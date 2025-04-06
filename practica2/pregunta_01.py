"""Reglas
- Crear una clase llamada Empleado donde sus atributos deben ser nombre,
edad, sueldo y de nacionalidad peruana, tendrá un método para solicitar su
nombre y otro para solicitar su edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su nuevo método
aumentoSueldo para incrementar su sueldo en un 30% (mínimo instanciar
la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente método que retorne un mensaje donde indique que: “En
el año 2025 tendrá XX años”, el año se ingresará por parámetro y la edad
es la edad que ya se ingresó (Mostrar por pantalla este valor)
2. Usando el concepto de herencia y encapsulación (para el atributo saldo)
para crear elsiguiente programa (3 ptos):"""


class Empleado:
    def __init__(self, nombre, edad, saldo, nacionalidad="peruana"):
        self.nombre = nombre
        self.edad = edad
        self._saldo = saldo  # Encapsulando saldo
        self.nacionalidad = nacionalidad

    def solicitar_nombre(self):
        return self.nombre

    def solicitar_edad(self):
        return self.edad

    def cumpleaños(self):
        self.edad += 1

    def aumento_sueldo(self):
        self._saldo *= 1.30
        return self._saldo

    def mensaje_edad(self, año):
        edad_en_año = self.edad + (año - 2025)
        return f"En el año {año} tendrá {edad_en_año} años."



empleado1 = Empleado("Carlos Pérez", 30, 1500)
empleado2 = Empleado("Ana García", 25, 1200)


nuevo_sueldo1 = empleado1.aumento_sueldo()
nuevo_sueldo2 = empleado2.aumento_sueldo()

print(f"El sueldo de {empleado1.solicitar_nombre()} después de aumentar es: {nuevo_sueldo1}")
print(f"El sueldo de {empleado2.solicitar_nombre()} después de aumentar es: {nuevo_sueldo2}")

print(empleado1.mensaje_edad(2030))
print(empleado2.mensaje_edad(2030))
