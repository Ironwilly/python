#Una tienda ofrece un descuento del 15% sobre el total de la compra y 
#un cliente desea saber cuanto deberá pagar finalmente por su compra.

compra = float(input("¿Cúal es la cantidad total de su compra? "))
descuento = (compra * 15)/100
total = compra - descuento
print("El descuento que se le hace a su compra es de %.2f euros "% (descuento))
print("El total de su compra con el descuento incluido es de %.2f euros"% (total))
