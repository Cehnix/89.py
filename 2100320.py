from random import randint

n = randint(2,7)
lista1 = [0]*n
lista2 = []

for i in range(n):
    lista1[i] = randint(1,100)
print(lista1)

for i in range(n):
    if lista1[i] % 2 == 0:
        lista2.append(lista1[i])

with open("numerospares", "w") as archivo:
    archivo.write(str(lista2))
with open("numerospares", "r") as archivo:
    contenido = archivo.read()
print(contenido)
