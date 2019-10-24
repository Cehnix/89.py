#Ejercicio 13.4
A = -2
B = -1
divisor = 0
contador = 0

while(A<B) or (A<0) or (B<0):
    B = int(input("B: "))
    A = int(input("A: "))

for i in range(B, A+1):
    for j in range(1, i):
        if(i%j == 0):
            divisor += 1
    if(divisor == 1):
        print(i)
        contador += 1
    divisor = 0
print("Cantidad de primos: ", contador)