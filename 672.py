#Ejercicio 13.7
A = -2
B = -1
suma = 0
perfecto = 0

while(A<B) or (A<0) or (B<0):
    B = int(input("Digite B: "))
    A = int(input("Digite A: "))

for i in range(B, A):
    for j in range(1, i):
        if(i%j == 0):
            perfecto += j
    if(perfecto == i):
        suma += i
    perfecto = 0
print("Suma de los perfectos: ", suma)
            