#Crea un programa que pida al usuario dos números y 
#muestre su división si el segundo no es cero, 
#o un mensaje de aviso en caso contrario.


numero1 = int(input("Diga el primer número: "))
numero2 = int(input("Diga el segundo número: "))

if (numero2 == 0):
    print("No se muestra la divisíon porque el segundo número es 0 ")
    

else:
    
    resultado = numero1/numero2
    print("El resultado de dividir el número %d entre el número %d es: %d" %(numero1,numero2,resultado))