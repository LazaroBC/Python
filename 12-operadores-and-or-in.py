# 
# salarioPresidente= int(input("Introduce salario presidente "))
# print("Salario presidente: " + str(salarioPresidente))
# 
# salarioDirector= int(input("Introduce salario director "))
# print("Salario director: " + str(salarioDirector))
# 
# salarioJefeArea= int(input("Introduce salario jefe area "))
# print("Salario Jefe Area: " + str(salarioJefeArea))
# 
# salarioAdministrativo= int(input("Introduce salario Administrativo "))
# print("Salario administrativo: " + str(salarioAdministrativo))
# 
# if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
#     print("Todo OK")
# else:
#     print("Revisa los datos")
# 

# print("Programa de becas")
# distanciaEscuela = int(input("Introduce la distancia a la escuela: "))
# print(distanciaEscuela)
# 
# numeroHermanos = int(input("Introduce el número de hermanos: "))
# print(numeroHermanos)
# 
# salarioFamiliar = int(input("Introduce salario familiar: "))
# print(salarioFamiliar)
# 
# if distanciaEscuela>40 or numeroHermanos>2 and salarioFamiliar<= 20000:
#     print("Tiene derecho a beca")
# else:
#     print("No tiene derechoa beca")

print("Asignaturas optativas ño 2021")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()
if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("No existe")