nombreTupla=('Lázaro', 1, True)

print(nombreTupla[1])

#convertir tupla en lista

nombreLista=list(nombreTupla)
print(nombreLista)

#convertir lista en tupla
nuevaTupla=tuple(nombreLista)
print(nuevaTupla)

#Encontrar un elemento
print(1 in nuevaTupla)

# Cuantas veces está un elemento en la tupla
print(nuevaTupla.count(1))

# averiguar logitud de una tupla o lista
print(len(nuevaTupla))

#Tupla sin parentesis(empaquetado de tuplas)
tupla2="Juan",1,2,3
print(tupla2)

#desempaquetado de tuplas, meter los valores variables
nombre, dia, mes, anyo=tupla2
print(nombre, dia, anyo, mes)


c=(1,2,3,4,5,6,7,8,9,0)
print(c[::2])

