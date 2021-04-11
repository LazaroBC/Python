numero = int(input("Introduce un número y te doy la lista del reves: "))

intentos = 0
while numero<=0:
    print("El número debe de ser mayor que 0 y positivo")
    if intentos ==2:
        print("Exceso de intentos")
        break
    numero=int(input("Introduce un número: "))
    if numero<0:
        intentos=intentos+1
n=numero
for i in range (numero):
    print(n, end=", ")
    n= n-1

n1 = int(input("Introduce un número entero positivo: "))
for i in range(n1, -1, -1):
    print(i, end=", ")