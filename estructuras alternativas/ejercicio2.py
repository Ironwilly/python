#Algoritmo que pida un número y diga si es positivo, negativo o 0.


numero = int(input("Diga un número: "))

if(numero <0):
    print("El número %d es negativo"%(numero))
elif(numero == 0):
    print("El número es 0 ")

else:
    print("El número %d es positivo"%(numero))

