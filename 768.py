#Ejercicio 13.3
A = -2
B = -1
contador = 0
perfecto = 0

while(A<B) or (A<0) or (B<0):
    B = int(input("Digite B: "))
    A = int(input("Digite A: "))

for i in range(B, A):
    for j in range(1, i):
        if(i%j == 0):
            perfecto += j
    if(perfecto == i):
        print(i)
        contador += 1
    perfecto = 0
print("Cantidad de perfectos: ", contador)
            