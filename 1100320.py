from random import randint

n = 2*randint(2,4)
lista = [0]*n

for i in range(n):
    lista[i] = randint(0,10)
print(lista)

medio = n//2

orden1 = sorted(lista)
orden2 = sorted(lista, reverse = True)

lista_ordenada = orden1[0:medio] + orden2[0:medio]
print(lista_ordenada)