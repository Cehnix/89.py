def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial*i
    return(factorial)

def suma_fact(n):
    suma_fact = 0
    factorial = 1
    for j in range(1, n+1):
        for i in range (1, j+1):
            factorial = factorial*i
        suma_fact += factorial
        factorial = 1
    return(suma_fact)

n = int(input("Digite un número: "))
resultado = suma_fact(n)
print(resultado)
