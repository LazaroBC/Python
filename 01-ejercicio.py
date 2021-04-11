print("Ejercicio 1")



def mensaje() :
    print("1")
    print("2")
    print("3")
    
    

mensaje()
print('')
print('Lo siguiente escribirlo con una función')

mensaje()
mensaje()
mensaje()
print('')
print('Escribirlo usando variables')
n1=1
n2=2
print('')
print('Suma: ' + str(n1) + ' + ' + str(n2) + ' = ' + str(n1 + n2))

print('')
print('Escribirlo usando una función (para nota)')

def escribir_suma(x, y):
    return 'El resultado de %i y %i es: %i' % (x, y, x+y)

print (escribir_suma(7, 8))

var = 2
if var%2 == 0:
    print("par")
else:
    print("impar")

imprimir = "par" if (var % 3 == 0) else "impar"

print(imprimir)

