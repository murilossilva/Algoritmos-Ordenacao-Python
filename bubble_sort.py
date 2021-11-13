import numpy.random as np

def bubbleSort(x):
    for i in range(len(x),0,-1):
        troca = False
        for j in range(0, i-1):
            if x[j] > x[j + 1] :
                x[j], x[j + 1] = x[j + 1], x[j]
                troca = True
        if not troca:
            break

x = np.randint(0, 1000, 50)            
bubbleSort(x), print(x)
