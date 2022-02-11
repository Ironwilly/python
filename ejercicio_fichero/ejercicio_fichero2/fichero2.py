#1. Realizar una aplicación que sea capaz de transformar un fichero
# CSV en un fichero .sql con sentencias insert into.
#- El nombre de la tabla sql será el nombre del fichero sin extensión.
#- Las columnas de la tabla vendrán determinadas por la fila de encabezado.
#- Como entrada, el programa recibirá un fichero csv con varias líneas, y como
# salida, sea obtendrá un fichero con extensión .sql con tantos
# INSERT INTO.... como línea tuviera el CSV.
#2. Realiza la herramienta inversa a la anterior, que reciba un
# fichero con una serie de sentencias INSERT INTO y lo transforme en un fichero .csv


import csv
import sqlite3


productos = [
        ("Cocacola", "1.10", "20"),
        ("Fanta", "1.05", "30"),
        ("Aquarius", "1.15", "15")
    ]

with open("productos.csv","w", newline="\n") as csvfile:
    campos = ["nombre", "precio", "cantidad"]
    writer = csv.DictWriter(csvfile, fieldnames= campos)
    writer.writeheader()
    for nombre, precio, cantidad in productos:
        writer.writerow({
            "nombre": nombre, "precio": precio, "cantidad": cantidad
        })

con = sqlite3.connect('mydatabase.db')

with open('productos.csv','r') as f:
    reader = csv.reader(f)
    columns = next(reader)

    cursor = con.cursor()
    for data in reader:
        cursor.execute("CREATE TABLE productos (nombre VARCHAR(255), precio INT(), cantidad INT()")
    cursor.commit()






