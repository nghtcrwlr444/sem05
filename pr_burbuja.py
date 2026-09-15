#Método burbuja
def met_burbuja(lista) -> list:
    num = len(lista)
    for mano_izq in range(num):
        for mano_der in range(0, num - mano_izq - 1):
            if lista[mano_der] > lista[mano_der + 1]:
                lista[mano_der], lista[mano_der + 1] = lista[mano_der + 1], lista[mano_der]
    return lista

lista = [2, 8, 5, 3, 9, 4, 1]
print(met_burbuja(lista))
