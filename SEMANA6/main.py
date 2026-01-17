"""
Tarea Semana 6 - POO
Tema: Clase, Objeto, Herencia, Encapsulación y Polimorfismo

Programa: Sistema simple de compras.
- Clase base: Producto
- Clase derivada: ProductoConDescuento (hereda de Producto)
- Encapsulación: precio es privado (__precio) y se controla con property
- Polimorfismo: calcular_total() se comporta diferente en la clase hija (sobrescritura)
"""

class Producto:
    """
    Clase base que representa un producto genérico.
    """

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.__precio = 0.0  # Encapsulación: atributo privado
        self.precio = precio  # Se asigna pasando por el setter (validación)

    # Encapsulación: Getter
    @property
    def precio(self) -> float:
        return self.__precio

    # Encapsulación: Setter con validación
    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio debe ser numérico (int o float).")
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = float(valor)

    def calcular_total(self, cantidad: int) -> float:
        """
        Calcula el total sin descuentos.
        Polimorfismo: este método será sobrescrito en la clase hija.
        """
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        return self.precio * cantidad

    def __str__(self) -> str:
        return f"Producto(nombre='{self.nombre}', precio=${self.precio:.2f})"


class ProductoConDescuento(Producto):
    """
    Clase derivada que aplica descuento.
    Herencia: reutiliza nombre y precio de Producto.
    Polimorfismo: sobrescribe calcular_total().
    """

    def __init__(self, nombre: str, precio: float, descuento: float):
        super().__init__(nombre, precio)
        self.descuento = descuento  # porcentaje: 0 a 100

    @property
    def descuento(self) -> float:
        return self.__descuento

    @descuento.setter
    def descuento(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise TypeError("El descuento debe ser numérico (int o float).")
        if valor < 0 or valor > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.__descuento = float(valor)

    def calcular_total(self, cantidad: int) -> float:
        """
        Polimorfismo (sobrescritura):
        Esta versión aplica descuento al total.
        """
        total_sin_descuento = super().calcular_total(cantidad)
        factor = 1 - (self.descuento / 100)
        return total_sin_descuento * factor

    def __str__(self) -> str:
        return (f"ProductoConDescuento(nombre='{self.nombre}', "
                f"precio=${self.precio:.2f}, descuento={self.descuento:.0f}%)")


def main():
    """
    Función principal:
    - Crea objetos (instancias)
    - Ejecuta métodos
    - Demuestra herencia, encapsulación y polimorfismo
    """
    print("=== SISTEMA DE COMPRAS (POO) ===\n")

    # Objetos (instancias)
    producto_normal = Producto("Cuaderno", 2.50)
    producto_desc = ProductoConDescuento("Audífonos", 18.00, 15)

    # Mostrar objetos (usa __str__)
    print("Objetos creados:")
    print(producto_normal)
    print(producto_desc)

    # Demostración de encapsulación (setter con validación)
    print("\nActualizando precio del cuaderno a $3.00 (encapsulación con property)...")
    producto_normal.precio = 3.00
    print(producto_normal)

    # Polimorfismo: mismo método, distinto comportamiento según el objeto
    print("\n=== Cálculos (Polimorfismo) ===")
    cantidad_1 = 4
    cantidad_2 = 2

    total_1 = producto_normal.calcular_total(cantidad_1)   # sin descuento
    total_2 = producto_desc.calcular_total(cantidad_2)     # con descuento (sobrescrito)

    print(f"Total de {cantidad_1} '{producto_normal.nombre}': ${total_1:.2f}")
    print(f"Total de {cantidad_2} '{producto_desc.nombre}' con {producto_desc.descuento:.0f}%: ${total_2:.2f}")

    # Extra: lista de objetos y polimorfismo en bucle
    print("\n=== Polimorfismo en una lista de objetos ===")
    carrito = [producto_normal, producto_desc]
    for item in carrito:
        print(f"{item.nombre} -> total x1 = ${item.calcular_total(1):.2f}")

    print("\nFin del programa.")


if __name__ == "__main__":
    main()
