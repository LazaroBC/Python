for i in [1,2,3]:
   print(str(i) +  " Hola", i)

email = False
for i in "lazarete@outlook.com":
    if (i=="@"):
        email = True

if email:
    print("Email correcto")
else:
    print("Email incorrecto")

for i in range(5):
    print (i)

edad = 0
while edad < 5:
    edad = edad + 1
    print ("Felicidades, tienes " + str(edad) + " años.")