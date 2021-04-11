def divide():
    try:
        op1=(float(input("Intrpduce el primer número: ")))
        op2=(float(input("Intrpduce el segundo número: ")))
        print("La división es: " + str(op1/op2))
    except:
        print("Ha ocurrido un error")

    finally:
        print("Cáculo realizado")
divide()
def divide2():
    try:
        op1=(float(input("Intrpduce el primer número: ")))
        op2=(float(input("Intrpduce el segundo número: ")))
        print("La división es: " + str(op1/op2))

    finally:
        print("Cáculo realizado")
divide2()