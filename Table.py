import pyodbc
import pandas as pd

conexion = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=ProduccionTony_Stark;"
    "Trusted_Connection=yes;"
)

cursor = conexion.cursor()

cursor.execute("SELECT Nombre FROM Datos")

datos = []

for fila in cursor.fetchall():
    datos.append(float(fila[0]))

# Valores base
menor = min(datos)
mayor = max(datos)

filas = 6

intervalo = (mayor - menor) / filas

tabla = []

liic = menor

for i in range(filas):

    lsic = liic + intervalo

    # Xi
    xi = (liic + lsic) / 2

    # Fi
    fi = 0

    for dato in datos:

        if dato >= liic and dato < lsic:
            fi += 1

    # FiXi
    fixi = fi * xi

    tabla.append([
        round(liic,2),
        round(lsic,2),
        fi,
        round(xi,2),
        round(fixi,2)
    ])

    liic = lsic

# Crear tabla
df = pd.DataFrame(
    tabla,
    columns=["LIIC","LSIC","Fi","Xi","FiXi"]
)

print(df)

conexion.close()