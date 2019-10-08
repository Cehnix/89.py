H = -1
M = -1
S = -1
tiempo = 0

while(H < 0) or (M < 0) or (S < 0):
    H = int(input("Digite la cantidad de horas: "))
    M = int(input("Digite la cantidad de minutos: "))
    S = int(input("Digite la cantidadd de segundos: "))
tiempo = 3600*H + 60*M + S
print(tiempo)
