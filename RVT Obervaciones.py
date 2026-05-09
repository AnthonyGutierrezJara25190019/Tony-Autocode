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

# Rango
rvt = mayor - menor

print("Valor mayor:", mayor)
print("Valor menor:", menor)
print("RVT:", rvt)

conexion.close()