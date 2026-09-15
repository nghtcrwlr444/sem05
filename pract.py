def metodo_seleccion(lista)-> list:
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

lista = [64, 25, 12, 22, 11]
print(metodo_seleccion(lista))