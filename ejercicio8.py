#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
#en cuenta su sueldo base y comisiones.

sueldobase = float(input("¿Cuás es su sueldo base?: "))
comision = ((sueldobase * 10)/100) * 3
sueldototal = sueldobase + comision
print("Pos las comisiones obtendrá %.2f euros "% (comision))
print("Su sueldo total con las comisiones sería %.2f euros"%(sueldototal))
