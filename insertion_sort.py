import numpy.random as np

def insertionSort(lista):
    for i in range(len(lista)):
        atual = lista[i]

        while i > 0 and lista[i - 1] > atual:
            lista[i] = lista[i - 1]
            i -= 1
            
        lista[i] = atual

lista = np.randint(0, 1000, 50) 
insertionSort(lista)
print(lista)

