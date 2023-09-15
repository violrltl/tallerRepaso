from dataclasses import dataclass

@dataclass

class Elemento:
    nombre: str


    def __eq__(self, other):
        if isinstance(self, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:

    contador= 0
    def __init__(self, nombre):
        self.elementos: list = []
        self.nombre: str = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento) ->bool:
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, otro_conjunto):
        nuevo_nombre = f"{self.nombre} UNION {otro_conjunto.nombre}"
        nuevo_conjunto = Conjunto(nuevo_nombre)

        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)

        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)

        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_resultante = f"{conjunto1.nombre} intersectado {conjunto2.nombre}"
        elementos_resultantes = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nuevo_conjunto = Conjunto(nombre_resultante)
        nuevo_conjunto.elementos = elementos_resultantes
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


elemento1= Elemento("e1")
elemento2 = Elemento("e2")
elemento3 = Elemento("e3")

conjunto1 = Conjunto("c1")
conjunto2 = Conjunto("c2")

conjunto1.agregar_elemento(elemento1)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento3)

union_conjuntos= conjunto1 + conjunto2

interseccion_conjuntos = Conjunto.intersectar(conjunto1, conjunto2)

print(conjunto1)
print(conjunto2)
print(union_conjuntos)
print(interseccion_conjuntos)
