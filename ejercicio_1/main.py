# Ejercicio 1. Cobro de estacionamiento


class Estacionamiento(object):
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        # La tarifa del rango se aplica a TODAS las horas
        if self.horas <= 2:
            tarifa = 15.00
        elif self.horas <= 5:
            tarifa = 12.00
        else:
            tarifa = 10.00
        return self.horas * tarifa

    def mostrarRecibo(self):
        total = self.calcularPago()
        print("RECIBO DE ESTACIONAMIENTO")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${total:.2f}")


# Programa principal
horas = 0
while horas <= 0:
    try:
        horas = int(input("Horas estacionadas: "))
        if horas <= 0:
            print("Error: las horas deben ser un número entero mayor que cero.")
    except ValueError:
        print("Error: debes escribir un número entero.")

estacionamiento1 = Estacionamiento(horas)
estacionamiento1.mostrarRecibo()
