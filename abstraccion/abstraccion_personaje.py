"""
Ejemplo de ABSTRACCIÓN en POO.

Abstracción = quedarnos solo con los datos y comportamientos
esenciales de un objeto, ocultando detalles que no son relevantes
para el problema que queremos resolver.
"""


class Personaje:
    def __init__(self, nombre: str, puntos_vida: int, puntos_ataque: int) -> None:
        # Solo modelamos lo esencial del personaje:
        # nombre, vida y ataque. No nos preocupamos por
        # armadura, inventario, historia, etc.
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.puntos_ataque = puntos_ataque

    def describir(self) -> None:
        """Muestra la información esencial del personaje."""
        print(f"Personaje: {self.nombre}")
        print(f"  Vida: {self.puntos_vida}")
        print(f"  Ataque: {self.puntos_ataque}")


if __name__ == "__main__":
    # Creamos algunos personajes con solo la información esencial.
    guerrero = Personaje("Guerrero", 120, 25)
    mago = Personaje("Mago", 80, 40)

    print("=== Ejemplo de ABSTRACCIÓN ===")
    guerrero.describir()
    print()
    mago.describir()
