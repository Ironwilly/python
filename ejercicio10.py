#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.


parcial1 = float(input("Diga la nota del parcial 1: "))
parcial2 = float(input("Diga la nota del parcual 2: "))
parcial3 = float(input("Diga la nota del parcial 3: "))

examenfinal = float(input("Diga la nota del examen final: "))
trabajofinal = float(input("Diga la nota del trabajo final: "))

promedio = (parcial1 + parcial2 + parcial3)/3

calificaciónfinal = (promedio * 55)/100 + (examenfinal * 30)/100 + (trabajofinal * 15)/100

print("La calificación final de la materia de algoritmos es de %.2f"%(calificaciónfinal))

