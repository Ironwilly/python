#Dadas dos variables numéricas A y B, 
#que el usuario debe teclear, 
# se pide realizar un algoritmo que 
# intercambie los valores de ambas variables 
# y muestre cuanto valen al final las dos variables.

a = int(input("Escribe el valor de A: "))
b = int(input("Escribe el valor de B: "))

aux = a
a = b
b = aux

print("El valor de A es : %d"% (a))
print("El valor de B es : %d"% (b))