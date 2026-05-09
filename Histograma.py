import pyodbc
import matplotlib.pyplot as plt

# Conexion SQL
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

conexion.close()

# Crear histograma
plt.hist(datos, bins=6)

# Titulos
plt.title("Histograma de Datos")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")

# Mostrar
plt.show()