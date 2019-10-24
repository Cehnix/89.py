#Ejercicio 13.5
A = 0
B = 1
suma = 0
while(A<B):
    A = int(input("Digite el primer número: "))
    B = int(input("Digite el segundo número: "))
    
if (A%2 == 0):
    if(B%2 == 0):
        print(A + B)
    else:
        print(A)
elif (A%2 != 0):
    if(B%2 == 0):
        print(B)
    else:
        print("No hay un númeo par")
