def metodo_seleccion(lista) -> list:
    num = len(lista)
    for mano_izq in range(num):
        min_index = mano_izq
        for mano_der in range(mano_izq + 1, num):
            if lista[mano_der] < lista[min_index]:
                min_index = mano_der
        if min_index != mano_izq:
            lista[mano_izq], lista[min_index] = lista[min_index], lista[mano_izq]
    return lista

lista = [2, 8, 5, 3, 9, 4, 1]
print(metodo_seleccion(lista))
