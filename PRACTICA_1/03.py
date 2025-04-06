nombre = "Alicia"
salario = 6000
edad = "32"
compania = "UNMSM"
bono= 36000600
trabaja_en_la_empresa=True
apellido = "Medrano"
cantidad_de_hijos= 0
lista =[]
lista.append(nombre)
lista.append(salario)
lista.append(edad)
lista.append(compania)
lista.append(bono)
lista.append(trabaja_en_la_empresa)
lista.append(apellido)
lista.append(cantidad_de_hijos)


print("los datos de la lista son:{}".format(lista))
if cantidad_de_hijos == 0:
    print("No cumple para obtener el bono familiar")
if cantidad_de_hijos >= 1:
    nuevo_valor=0.8 *salario
    print("Obtienen el bono familiar el cual es de : {}".format(nuevo_valor))

print("-----------------------------------------------------------------------------")
print("los datos de la lista son:{}".format(lista))