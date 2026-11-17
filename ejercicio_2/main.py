# Ejercicio 2. Calculadora con herencia


class Operacion(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2

    def mostrarResultado(self):
        print(self.calcular())


class Resta(Operacion):
    # No necesita __init__: hereda el de Operacion
    def calcular(self):
        return self.numero1 - self.numero2


def pedirNumero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debes escribir un número entero.")


# Programa principal
numero1 = pedirNumero("Número 1: ")
numero2 = pedirNumero("Número 2: ")

suma = Operacion(numero1, numero2)
resta = Resta(numero1, numero2)

print("Resultado de la suma: ", end="")
suma.mostrarResultado()
print("Resultado de la resta: ", end="")
resta.mostrarResultado()
