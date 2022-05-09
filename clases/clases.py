import math


class BadRequest(Exception):
    pass


class Circulo:
    def __init__(self, radio):
        self.set_radio(radio)

    def set_radio(self, radio):
        try:
            self._isValidRadio(radio)
            self.radio = radio
            self.calcula_area()
            self.calcula_perimetro()
        except BadRequest as exc:
            print(exc)

    def calcula_area(self):
        self.area = round(math.pi*(self.radio**2), 2)
        return self.area

    def calcula_perimetro(self):
        self.perimetro = round(2*math.pi*self.radio, 2)
        return self.perimetro

    def _isValidRadio(self, radio):
        if radio <= 0:
            raise BadRequest("ERROR: No se puede asignar un radio <= 0")
        return True

    def _isValidMultiplicacion(self, numero):
        if numero <= 0:
            raise BadRequest(
                "ERROR: No se permite la multiplicacion por numeros <= 0")
        return True

    def __mul__(self, numero):
        try:
            self._isValidMultiplicacion(numero)
            return Circulo(self.radio * numero)
        except BadRequest as exc:
            print(exc)

    def __repr__(self):
        return f"El circulo tiene un radio de {self.radio}, un area de {self.area} y un perimetro de {self.perimetro}"


circulo = Circulo(int(input("Ingresar el radio del circulo")))
print(circulo)
respuesta = input("Desea modificar el radio? s/n")
if respuesta.lower() == 's':
    circulo.set_radio(int(input("Ingresar nuevo radio")))
    print(circulo)
respuesta = input("Desea multiplicar el circulo? s/n")
if respuesta.lower() == "s":
    circulo2 = circulo * int(input("Ingresar numero con el que se va a multiplicar el circulo"))
    print(circulo2)
