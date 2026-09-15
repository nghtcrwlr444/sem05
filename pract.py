def metodo_seleccion(lista) -> list:
    num = len(lista) 
    
    for i in range(num): 
        min_index = i
        for j in range(i + 1, num): 
            if lista[j] < lista[min_index]:
                min_index = j
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

lista = [2, 9, 5, 4, 8]
print(metodo_seleccion(lista))
