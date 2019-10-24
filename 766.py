#Ejercicio 13.1
contador = 0
A = -2
B = -1
while(A<B) or (A<0) or (B<0):
    A = int(input("Digite el primer número: "))
    B = int(input("Digite el segundo número: "))
    
if (A%2 == 0):
    contador += 1
    if(B%2 == 0):
        contador += 1
        print(A, B, "Contador: ", contador)
    else:
        print(A, "Contador: ", contador)
elif (A%2 != 0):
    if(B%2 == 0):
        contador += 1
        print(B, "Contador: ", contador)
    else:
        print("No hay un número par")


