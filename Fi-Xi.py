import pyodbc

conexion = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=ProduccionTony_Stark;"
    "Trusted_Connection=yes;"
)

cursor = conexion.cursor()

# Leer datos
cursor.execute("SELECT Nombre FROM Datos")

datos = []

for fila in cursor.fetchall():
    datos.append(float(fila[0]))

# Menor y mayor
menor = min(datos)
mayor = max(datos)

# Numero de clases
filas = 6

# Intervalo
intervalo = (mayor - menor) / filas

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
    #FI -Frecuencia ponderada
    #XI - Marca de clase

    print("Fila", i + 1)
    print("LIIC:", round(liic, 2))
    print("LSIC:", round(lsic, 2))
    print("Xi:", round(xi, 2))
    print("Fi:", fi)
    print("FiXi:", round(fixi, 2))
    print("------------------------")

    liic = lsic

conexion.close()