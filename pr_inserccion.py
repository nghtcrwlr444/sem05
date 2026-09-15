#Método insercción
def met_insercion(lista) -> list:
    num = len(lista)
    for mano_izq in range(1, num):
        clave = lista[mano_izq]
        mano_der = mano_izq - 1
        while mano_der >= 0 and lista[mano_der] > clave:
            lista[mano_der + 1] = lista[mano_der]
            mano_der -= 1
        lista[mano_der + 1] = clave
    return lista

lista = [2, 8, 5, 3, 9, 4, 1]
print(met_insercion(lista))
