from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elemento == e for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, otro_conjunto):
        nuevo_nombre = f"{self.nombre} UNION {otro_conjunto.nombre}"
        nuevo_conjunto = Conjunto(nuevo_nombre)
        nuevo_conjunto.elementos.extend(self.elementos)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nuevo_nombre)
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.elementos)
        return f"Conjunto '{self.nombre}' (ID: {self.id}): {{{elementos_str}}}"

# Ejemplo de uso:
if __name__ == "__main__":
    elemento1 = Elemento("A")
    elemento2 = Elemento("B")
    elemento3 = Elemento("C")

    conjunto1 = Conjunto("Conjunto 1")
    conjunto1.agregar_elemento(elemento1)
    conjunto1.agregar_elemento(elemento2)

    conjunto2 = Conjunto("Conjunto 2")
    conjunto2.agregar_elemento(elemento2)
    conjunto2.agregar_elemento(elemento3)

    print(conjunto1)
    print(conjunto2)

    conjunto_union = conjunto1 + conjunto2
    print(conjunto_union)

    conjunto_interseccion = Conjunto.intersectar(conjunto1, conjunto2)
    print(conjunto_interseccion)
