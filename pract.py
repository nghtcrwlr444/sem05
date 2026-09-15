def metodo_seleccion(lista) -> list:
    num = len(lista)
    
    for val_min in range(num):
        min_index = val_min
        for val_max in range(val_min + 1, num):
            if lista[val_max] < lista[min_index]:
                min_index = val_max
        if min_index != val_min:
            lista[val_min], lista[min_index] = lista[min_index], lista[val_min]
    return lista

lista = [2, 8, 5, 3, 9, 4, 1]
print(metodo_seleccion(lista))
