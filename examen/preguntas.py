# Parte 1. Interpretación y complementación 


# Actividad 1. Identificar elementos de POO


class Producto(object):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.total = 0

    def calcularTotal(self, cantidad):
        self.total = self.precio * cantidad

    def mostrarTotal(self):
        print(f"Producto: {self.nombre}")
        print(f"Total: ${self.total:.2f}")


producto1 = Producto("Cuaderno", 35)
producto1.calcularTotal(3)
producto1.mostrarTotal()

# 1. ¿Cuál es el nombre de la clase?
# Producto 

# 2. ¿Cuáles son sus propiedades?
# nombre, precio y total 

# 3. ¿Cuáles son sus métodos?
# __init__ (constructor), calcularTotal y mostrarTotal.

# 4. ¿Qué función cumple __init__?
# Es constructor. Se ejecuta automáticamente al crear un objeto y sirve para dar los valores iniciales a sus propiedades, (nombre, precio y total = 0).

# 5. ¿Para qué se utiliza self?
# representa al objeto que está usando el método. Sirve para:
#  guardar y leer las propiedades de ese objeto en particular
#  para llamar a sus otros métodos 

# 6. ¿En qué instrucción se crea un objeto?
# producto1 = Producto("Cuaderno", 35) se crea un objeto de la clase Producto y se guarda en la variable producto1.

# 7. ¿Cuál es el nombre del objeto?
#  producto1.

# 8. ¿Cómo se llama a calcularTotal()?
# Con el nombre del objeto, un punto y el método con su argumento: producto1.calcularTotal(3)

# 9. ¿Qué valores recibe el constructor cuando se crea el objeto?
# nombre = "Cuaderno" y precio = 35 

# 10. ¿Qué resultado mostrará el programa?
#    Producto: Cuaderno
#    Total: $105 


# Actividad 2. Completar código

class Rectangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def mostrarArea(self):
        print(f"El área del rectángulo es: {self.calcularArea()}")


rectangulo1 = Rectangulo(8, 5)
rectangulo1.mostrarArea()


# Actividad 3. Interpretar herencia 

class Operacion(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2


class Multiplicacion(Operacion):
    def calcular(self):
        return self.numero1 * self.numero2


operacion1 = Operacion(8, 4)
operacion2 = Multiplicacion(8, 4)
print(operacion1.calcular())
print(operacion2.calcular())

# 1. ¿Cuál es la clase padre?
# Operacion

# 2. ¿Cuál es la clase hija?
# Multiplicacion

# 3. ¿Cómo se indica la herencia?
#  Escribiendo la clase padre entre paréntesis al definir la clase hija: class Multiplicacion(Operacion):

# 4. ¿Qué propiedades utiliza la clase hija?
# numero1 y numero2, las hereda de Operacion.

# 5. ¿Por qué puede utilizarlas sin definir su propio __init__?
# Pq al no tener __init__ propio, hereda el __init__ de Operacion.
#    Al hacer Multiplicacion(8, 4) se ejecuta el constructor del padre, que guarda self.numero1 = 8 y self.numero2 = 4 en el objeto. 

# 6. ¿Por qué los métodos calcular() tienen resultados distintos?
# porque multiplicacion sobrescribe el método calcular.
#    El objeto de Operacion usa la versión del padre (suma) y el objeto de Multiplicacion usa su propia versión (multiplicación).

# 7. ¿Qué valores se imprimen?
# Resp: 12  (8 + 4, de operacion1)
#    32  (8 * 4, de operacion2)

# 8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
# R: usaría el calcular() heredado de Operacion, así que operacion2.calcular() también sumaría y se imprimiría 12 dos veces.
