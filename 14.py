N = int(input("N: "))
n = 0

positivos = 0
negativos = 0

sumap = 0
suman = 0

for i in range(1, N+1):
    n = int(input("Digite número: "))
    if(n > 0):
        print("Positivos: ", n)
        positivos += 1
        sumap += n
    elif(n < 0):
        print("Negativos: ", n)
        negativos += 1
        suman += n
print("La suma de los positivos: ", sumap)
print("La suma de los negativos: ", suman)

promediop = sumap/N
promedion = suman/N

print("El promedio de los positivos es: ", promediop)
print("El promedio de los negativos es: ", promedion)
        
        
    