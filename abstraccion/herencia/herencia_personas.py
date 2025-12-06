"""
Ejemplo de HERENCIA en POO.

Herencia = crear nuevas clases basadas en una clase existente,
reutilizando atributos y métodos.
"""


class Persona:
    def __init__(self, nombre: str, correo: str) -> None:
        self.nombre = nombre
        self.correo = correo

    def presentarse(self) -> None:
        print(f"Hola, soy {self.nombre}. Mi correo es {self.correo}.")


class Estudiante(Persona):
    def __init__(self, nombre: str, correo: str, matricula: str) -> None:
        super().__init__(nombre, correo)
        self.matricula = matricula

    def presentarse(self) -> None:
        # Sobrescribimos el método para agregar información
        print(f"Soy el estudiante {self.nombre}, matrícula {self.matricula}.")


class Profesor(Persona):
    def __init__(self, nombre: str, correo: str, materia: str) -> None:
        super().__init__(nombre, correo)
        self.materia = materia

    def presentarse(self) -> None:
        print(f"Soy el profesor {self.nombre} y dicto la materia de {self.materia}.")


if __name__ == "__main__":
    print("=== Ejemplo de HERENCIA ===")
    estudiante = Estudiante("Bicker Rodríguez", "bicker@uea.edu.ec", "ITIC-001")
    profesor = Profesor("Ing. Nogales", "snogales@uea.edu.ec", "Programación Orientada a Objetos")

    estudiante.presentarse()
    profesor.presentarse()
