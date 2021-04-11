

# i=1
# 
# while i<=10:
#     print("Ejecución " +str((i)))
#     i = i+1
# 
# print("Terminó la ejecución")
# 
# print("---------")
# 
# edad=(int(input("Introduce la edad: ")))
# 
# while edad<0 or edad>100:
#     print("Hasintroducido una edad negativa.pruebaotra edad")
#     edad=int(input("Introduce correctamente la edad,por favor: "))
#     
# 
# print("Gracias")
# print("Edad: " + str(edad))


import math

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un númeropor favor: "))
intentos = 0
while numero<0:
    print("No se puede hallar la raíz cuadradadeunnúmero negativo")
    if intentos ==2:
        print("Exceso de intentos")
        break
    numero=int(input("Introduce un número: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raíz cuadrada es: " + str(solucion))