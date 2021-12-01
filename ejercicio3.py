#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1 = float(input("Dime el valor del cateto 1: "))
cateto2 = float(input("Dime el valor del cateto 2: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("El resultado de la hipotenusa es %.2f"%(hipotenusa))

