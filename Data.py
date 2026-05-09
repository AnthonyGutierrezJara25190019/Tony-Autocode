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

mayor = max(numeros)
menor = min(numeros)

print("Numero mayor:", mayor)
print("Numero menor:", menor)

conexion.close()

