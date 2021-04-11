# print("Programa Evaluación notas de alumnos")
# 
# notaAlumno = input("Introduce la nota del alumno: ")
# 
# def evaluacion(nota):
#     valoracion="aprobado"
#     if nota<5:
#         valoracion="suspendido"
#     return valoracion
# 
# print (evaluacion(int(notaAlumno)))

# 7print("Verificación de acceso")
# 7
# 7edadUsuario=int(input("Introduce edad: "))
# 7if edadUsuario<18:
# 7    print("No puede pasar")
# 7elif edadUsuario>100:
# 7    print("Edad incorrecta")
# 7else:
# 7    print("Puede pasar")
# 7
# 7print("Fin programa")

print("Verificación de acceso")

notaAlumno=int(input("Introduce tu nota: "))

if notaAlumno<5:
    print("Insuficiente")
elif notaAlumno<6:
    print("Suficiente")
elif notaAlumno<7:
    print("Bien")
elif notaAlumno<9:
    print("Notable")
else:
    print("Sobresaliente")

print("Fin programa")
