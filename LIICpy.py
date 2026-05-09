menor = 2.6
mayor = 6.5
filas = 6

intervalo = (mayor - menor) / filas

liic = menor

for i in range(filas):

    lsic = liic + intervalo

    print("Fila", i + 1)
    print("LIIC:", round(liic, 2))
    print("LSIC:", round(lsic, 2))
    print("----------------")

    liic = lsic