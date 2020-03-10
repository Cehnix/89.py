from random import randint

n = randint(3,7)
lista = [0]*n

for i in range(n):
    lista[i] = randint(1,10)
print(lista)

orden1 = sorted(lista)
print(orden1)

orden2 = sorted(lista, reverse = True)
print(orden2)

