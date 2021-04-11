diccionario={"Alemania":"Berlin","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
print(diccionario["Francia"])
print(diccionario)

# Agregar elementos
diccionario["Italia"]="Lisboa"
print(diccionario)

# Modificar un valor
diccionario["Italia"]="Roma"
print(diccionario)

# Eliminar elemento
del diccionario["Reino Unido"]
print(diccionario)

diccionario2={"Alemania":"Berlin",23:"París","Reino Unido":65,"España":True}
print(diccionario2)

tupla=("España","Francia", "Portugal")
diccionario3={tupla[0]:"Madrid",tupla[1]:"París",tupla[2]:"Lisboa"}
print(diccionario3)

#Añadir varios valores a una clave
diccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1993,1994]}
print(diccionario4)
diccionario5={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1991,1993,1994]}}
print(diccionario5)

print(diccionario5.keys())
print(diccionario5.values())
print(len(diccionario5))