import pyodbc

conexion = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=ProduccionTony_Stark;"
    "Trusted_Connection=yes;"
)

cursor = conexion.cursor()

cursor.execute("SELECT Nombre FROM Datos")

numeros = []

for fila in cursor.fetchall():
    numeros.append(float(fila[0]))

# Mayor y menor
mayor = max(numeros)
menor = min(numeros)

# RCT o rango
rct = mayor - menor

# Numero de filas
filas = len(numeros)

# RVLC
rvlc = rct / 6

print("Mayor:", mayor)
print("Menor:", menor)
print("RCT:", rct)
print("Filas:", filas)
print("RVLC:", rvlc)

conexion.close()