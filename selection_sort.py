import numpy.random as np

def selectionSort(lista):
    for i in range(0, len(lista)):
        menor_i = i
        for atual in range(i + 1, len(lista)):
            if lista[atual] < lista[menor_i]:
                menor_i = atual
            
        lista[i], lista[menor_i] = lista[menor_i], lista[i]

lista = np.randint(0, 1000, 50)
selectionSort(lista)
print(lista)
            
