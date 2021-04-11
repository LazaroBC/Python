class Coche():
    def __init__(self):
        
        self.__largoChasis = 250#( Encapsulada, solo se tiene acceso desde dentro de la clase)
        self.__anchoChasis = 120
        self.__ruedas = 4 
        self.__enMarcha = False#(Sin encapsular)

    def arrancar(self, arrancar):
        self.__enMarcha = arrancar
        if(self.__enMarcha):
            chequeo = self.__chequeoInterno()
        if (self.__enMarcha and chequeo):
            return "En marcha"
        elif(self.__enMarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "Parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)

    def __chequeoInterno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite= "ok"
        self.puertas = "ok"

        if (self.gasolina=="ok" and self.aceite == "ok" and self.puertas == "ok"):
            return True
        else:
            return False
        

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------Segundo objeto---------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()