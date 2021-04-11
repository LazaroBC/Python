for letra in "Python":
    
    if letra == "h":
        continue
    print("Letra: " + letra)

nombre = "Pildoras informáticas"
print(len(nombre))
contador = 0
for i in nombre:
    if i == " ":
        continue
    contador+=1

print(contador)

#Pass:devuelve null

# while True:
    # pass

# else
email = input("Introduce tu email: ")
for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba = False

print(arroba)