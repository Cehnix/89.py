a = int(input("Digite un primer número: "))
b = int(input("Digite un segundo número: " ))
c = int(input("Digite un tercer número: "))

if(a<=b) and (a<=c):
    if(b<=c):
        print(a,b,c)
    elif(c<=b):
        print(a,c,b)
elif(b<=a) and (b<=c):
    if(a<=c):
        print(b,a,c)
    elif(c<=a):
        print(b,c,a)
elif(c<=b) and (c<=a):
    if(b<=a):
        print(c,b,a)
    elif(a<=b):
        print(c,a,b)


    