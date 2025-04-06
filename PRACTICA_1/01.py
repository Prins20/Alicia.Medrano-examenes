nombre = "Alicia"
salario = 6000
edad = "32"
compania = "UNMSM"

"""convertie edad a numero"""
edad=int(edad)

"""condicionel-1"""
if edad >30:
    bono = 0.10
    print("Usted tiene un bono de 10% en el mes de diciembre")
if edad <= 30:
    bono = 0.05
    print("Usted tiene un bono del 5% en el mes diciembre")

print("--------------------------------------------------------------------------------------------------------------")

"""Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda"""
Bono_final= (salario**2) + (salario * bono)
print("El Bono final que tendra {} es :".format(Bono_final))