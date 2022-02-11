#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);


numero1 = int(input("Diga el primer número: "))
numero2 = int(input("Diga el segundo número: "))
numero3 = int(input("Diga el tercer número: "))

if(numero1 > numero2 and numero2 > numero3):
    print(numero1,numero2,numero3)
elif(numero2 > numero1 and numero1 > numero3):
    print(numero2,numero1,numero3)
elif(numero3 > numero1 and numero1 > numero2):
    print(numero3,numero1,numero2)
elif(numero3 > numero2 and numero2 > numero1):
    print(numero3,numero2,numero1)
    



