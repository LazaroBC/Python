# Extraen valores de una función almacenándolos en objetos iterables.

def generarPares(limite):
    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)

        num=num+1
    return miLista

print(generarPares(10))

print("--------")

def generarPares(limite):

    num=1
    
    while num<limite:
        yield num*2
        num=num+1
devuelvePares=generarPares(10)

print(next(devuelvePares))
print("Aquí podríair micódigo...")
print(next(devuelvePares))
print("Aquí podríair micódigo...")
print(next(devuelvePares))

for i in devuelvePares:
    print(i)

# yield from

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento

ciudades_devueltas=devuelveCiudades("Madrid", "Valencia", "Bilbao","Malaga")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
