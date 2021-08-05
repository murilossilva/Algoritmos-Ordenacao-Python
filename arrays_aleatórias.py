import numpy.random as np

a = int(input("Digite o menor número possível da lista: "))
b = int(input("Digite o maior número possível da lista: "))
c = int(input("Digite a quantidade de números a serem sorteados: "))
d = int(input("1 - Em ordem descrente \n2 - Em ordem crescente \n3 - Sem ordenação \n"))
x = np.randint(a,b,c)

def bubbleSort(x):
    n = len(x)
    if d == 1:
        for i in range(n):
            for j in range(0, n-i-1):
                if x[j] < x[j + 1] :
                    x[j], x[j + 1] = x[j + 1], x[j]
    if d == 2:
        n = len(x)
        for i in range(n):    
            for j in range(0, n-i-1):
                if x[j] > x[j + 1] :
                    x[j], x[j + 1] = x[j + 1], x[j]
                
bubbleSort(x), print(x)
