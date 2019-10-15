n = -1
suma = 0

while(n<=0):
    n = int(input("Digite el número: "))


for i in range(1,n):
    if(n%i == 0):
        suma += i
if(suma == n):
    print("Es un número perfecto")
else:
    print("No es un número perfecto")
        
        