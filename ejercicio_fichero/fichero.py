# Lee el fichero y procésalo de tal manera que sea capaz de mostrar
# la temperatura máxima para una ciudad dada. Esa ciudad la debe poder
# recibir como un argumento de entrada. Si la ciudad no existe, se deberá
# manejar a través de una excepción.


import csv

provincia = input('Diga el nombre de la ciudad: ')

with open("climatologia.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    try:

        for row in reader:

            if (provincia == row[2]):
                temperatura_maxima = row[3]

                print(f"provincia: '{provincia}' con temperatura maxima de {temperatura_maxima}")

            else:
                raise Exception("No existe ninguna ciudad: " + provincia)
    except Exception as cityNotFound:
        print(cityNotFound)
