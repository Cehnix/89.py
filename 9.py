n = int(input("Numero: "))
binario = 0
resto = 0
texto = ""

for i in range(0, 8):
    resto = n%2
    n = int(n/2)
    binario =+ resto
    texto += str(binario)
print(texto)
        