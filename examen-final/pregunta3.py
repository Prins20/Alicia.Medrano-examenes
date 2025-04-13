"""3. (3 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador

Reglas:

- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”

- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora

- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.

- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""
from datetime import datetime


def decorador_hora(func):
    def wrapper(**kwargs):
        ahora = datetime.now()
        hora = ahora.hour
        minuto = ahora.minute
        print("El decorador está siendo ejecutado a las {} horas"
              " con {} minutos".format(hora, minuto))

        suma = sum(kwargs.values())
        print("La suma de los valores es {}:".format(suma))

        resultado = func(**kwargs)
        print("La función fue ejecutada correctamente")
        return resultado
    return wrapper

@decorador_hora
def encontrar_mayor(**numeros):
    mayor = max(numeros.values())
    print("El mayor de todos los valores es {}:" .format(mayor))


encontrar_mayor(a=10, b=20, c=5, d=30, e=25, f=15)
encontrar_mayor(x=100, y=200, z=50)
encontrar_mayor(n1=1, n2=2, n3=3, n4=4, n5=5, n6=6)
