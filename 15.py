texto = str(input("Escriba un texto: "))
n = "0123456789"
c = 0

for i in n:
    for j in texto:
        if (j == i):
            c += 1
print(c)
