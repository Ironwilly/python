#Un ciclista parte de una ciudad A a las HH horas, 
# MM minutos y SS segundos. El tiempo de viaje hasta llegar 
# a otra ciudad B es de T segundos. Escribir un algoritmo 
# que determine la hora de llegada a la ciudad B.


horasalida = int(input("Hora de salida: "))
minutossalida = int(input("Minutos de salida: "))
segundossalida = int(input("Segundos de salida: "))
segundosviaje = int(input("Segundos de viaje: "))

segundossalidainicial = horasalida * 3600 + minutossalida * 60 + segundossalida

segundostotalviaje = segundossalidainicial + segundosviaje

horallegada = segundostotalviaje // 3600
minutosllegada = (segundostotalviaje % 3600) // 3600
segundosllegada = (segundostotalviaje % 3600) % 60

print("Hora de llegada ")
print(horallegada,":",minutosllegada,":",segundosllegada)


