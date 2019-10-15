def perfecto(n):
    suma = 0
    for i in range(1, n+1):
        for j in range(1,i):
            if(i%j == 0):
                suma += j
        if (suma == i):
            print(suma)
        suma = 0
    
#n = 1000
n = int(input("Digite un número: "))
p = perfecto(n)

print(p)