import pyodbc
import numpy as np
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

# Calcular media y desviacion
media = np.mean(datos)
desviacion = np.std(datos)

# Histograma
plt.hist(datos, bins=6, density=True)

# Campana de Gauss
x = np.linspace(min(datos), max(datos), 100)

y = (1 / (desviacion * np.sqrt(2 * np.pi))) * \
    np.exp(-(x - media)**2 / (2 * desviacion**2))

plt.plot(x, y)

# Titulos
plt.title("Campana de Gauss")
plt.xlabel("Valores")
plt.ylabel("Densidad")
print("Media:", media)
print("Desviación Estándar:", desviacion)


plt.show()


