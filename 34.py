n = int(input("Digite el número: "))
resto = 0
binario = ""

for i in range(0,8):
    resto = n%2
    n = int(n/2)
    binario += str(resto)
print(binario)
    