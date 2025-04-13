""" 2. (3 ptos) Crear un decorador conteo.

Reglas:
 El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
 Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
 La función que vas a crear va a capturar, la edad, nombre de un alumnos y la
hora y el minuto en que fue registrado (usar la librería correspondiente)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
 La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""
from datetime import datetime


def conteo(func):
    def wrapper(*args, **kwargs):
        total_parametro = len(args)+ len(kwargs)
        if total_parametro <= 1:
            return "Se requiere mas de un parametro para ejecutar la funcion"
        resultado = func(*args,**kwargs)
        print("la funcion fue ejecutada")
        return resultado
    return wrapper


@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute
    media =(nota1 + nota2+ nota3 + nota4) / 4

    print("{} de {} años ha sido registrda a las {} con {} minutos ".format(nombre,edad,hora,minuto))
    print("El promedio de notas es : {}".format(media))


registrar_alumno("Alicia",33,15,15,15,15)