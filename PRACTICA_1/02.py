
nombre = "Alicia"
salario = 6000
edad = "32"
compania = "UNMSM"
bono= 36000600
lista =[]
lista.append(nombre)
lista.append(salario)
lista.append(edad)
lista.append(compania)
lista.append(bono)

print("los datos de la lista son:{}".format(lista))
print("-------------------------------------------------")

trabaja_en_la_empresa=True
lista.append(trabaja_en_la_empresa)
print("los datos de la lista son:{}".format(lista))


print("----------------------------------------------------")
apellido = "Medrano"
trabaja_en_la_empresa=True
if trabaja_en_la_empresa == True:
    print("La trabajadora {} {} se encuntra trabajando actualemte en la compañia".format(nombre,apellido))
if trabaja_en_la_empresa == False:
    print("La trabajadora {} {} no se encuntra trabajando actualemte en la compañia".format(nombre,apellido))