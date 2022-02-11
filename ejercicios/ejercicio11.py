#Pide al usuario dos números y muestra la “distancia” entre ellos 
#(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).


import math
numero1 = int(input("Diga el primer número: "))
numero2 = int(input("Diga el segundo número: "))

distancia = math.fabs(numero1 - numero2)

print("La distancia entre los dos números indicados es de %d "% (distancia))
