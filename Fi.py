import pyodbc

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

menor = min(datos)
mayor = max(datos)

filas = 6

intervalo = (mayor - menor) / filas

liic = menor

total_fi = 0

for i in range(filas):

    lsic = liic + intervalo

    fi = 0

    for dato in datos:

        if dato >= liic and dato < lsic:
            fi += 1

    total_fi += fi

    print("Fila", i + 1)
    print("LIIC:", round(liic, 2))
    print("LSIC:", round(lsic, 2))
    print("Fi:", fi)
    print("----------------")

    liic = lsic

print("TOTAL:", total_fi)

conexion.close()