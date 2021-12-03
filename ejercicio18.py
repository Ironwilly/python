#Pedir el nombre y los dos apellidos de una persona 
# y mostrar las iniciales.

nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]


inicial = inicial.upper()
print("Las iniciales de tu nombre son: %s"%(inicial))

