lista1=['Luis','Lázaro','Pepe','Marta']

print(lista1[:])
print(lista1[2])
print(lista1[-2])

#Acceder a una porción de lista
print(lista1[0:2])
print(lista1[1:3])
print(lista1[:2])
print(lista1[2:])

#Agregar un elemento al final de la lista
lista1.append('Sandra') 
print(lista1[:])

#Insertar un elemnto en un lugar concreto de la lista
lista1.insert(2,'Raquel')
print(lista1[:])

#Agregar varios elementos
lista1.extend(['Jorge', 'Lourdes'])
print(lista1[:])

#Indica el indice, en el caso de que haya dos elementos iguale devuelve el primero
print(lista1.index('Raquel'))

#Indicar si un elemento existe
print('Raquel' in lista1)
print('Raque' in lista1)

lista2=[1, True, 'Carlos']
print(lista2[:])
#Eliminar un elemento
lista2.remove(1)
print(lista2[:])

#Eliminar el último elemento
lista2.pop()
print(lista2[:])

#concatenar listas
lista3=['Sandra', 'Lucia']
lista4=[1,'Pedro']
lista5=lista3+lista4
print(lista5[:])

#Multiplicar listas pero no crea una lista nueva
print(lista5[:] * 3)
print(lista5[:])

#Multiplicar un lista y sustituirla
lista6 = lista4 * 3
print(lista6[:])

n = lista6*len(lista6)

print(n)