
""" 1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):

Reglas:

- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola.
- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo
 """
import random


def generar_lista():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista generada:", lista)
    return lista


def numeros_no_repetidos(lista):
    sin_repetidos = list(set(lista))
    print("Lista sin números repetidos:", sin_repetidos)
    return sin_repetidos


def ordenar_lista(lista):
    descendente = sorted(lista, reverse=True)
    ascendente = sorted(lista)
    print("Orden descendente:", descendente)
    print("Orden ascendente:", ascendente)

    return descendente, ascendente


def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        mayor = max(pares)
        print("Mayor número par:", mayor)
        return mayor
    else:
        print("No hay números pares en la lista.")
        return None
