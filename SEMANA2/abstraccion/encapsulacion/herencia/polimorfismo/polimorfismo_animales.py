"""
Ejemplo de POLIMORFISMO en POO.

Polimorfismo = distintos objetos responden de forma diferente
al mismo mensaje (método), compartiendo una interfaz común.
"""


class Animal:
    def hablar(self) -> None:
        """Método que será redefinido en las subclases."""
        raise NotImplementedError("Este método debe ser implementado por la subclase")


class Perro(Animal):
    def hablar(self) -> None:
        print("El perro dice: ¡Guau!")


class Gato(Animal):
    def hablar(self) -> None:
        print("El gato dice: ¡Miau!")


class Vaca(Animal):
    def hablar(self) -> None:
        print("La vaca dice: ¡Muuu!")


def hacer_hablar(animal: Animal) -> None:
    """Función que usa polimorfismo: no le importa el tipo exacto de animal."""
    animal.hablar()


if __name__ == "__main__":
    print("=== Ejemplo de POLIMORFISMO ===")
    animales = [Perro(), Gato(), Vaca()]

    for a in animales:
        hacer_hablar(a)
