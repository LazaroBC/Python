
for i in range(5):
    print(f"Valor de la variable {i}")
print("-------")
for i in range(5,10):
    print(f"Valor de la variable {i}")
print("-------")
for i in range(5,50,5):
    print(f"Valor de la variable {i}")
print("-------")

valido=False
email=input("Email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")