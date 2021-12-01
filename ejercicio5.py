#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
#Recordar que la fórmula para la conversión es:
#C = (F-32)*5/9

Fahrenheit=float(input("Escribe un valor en grados Fahrenheit "))
c= (Fahrenheit-32)*5/9
print("%.2f grados Fahrenheit son %.2f grados Celsius"%(Fahrenheit,c))


