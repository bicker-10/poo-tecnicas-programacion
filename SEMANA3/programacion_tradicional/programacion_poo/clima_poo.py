"""
Programa en Programación Orientada a Objetos (POO)
para calcular el promedio semanal del clima.
Se utilizan clases, encapsulamiento y métodos.
"""

class ClimaSemanal:
    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Permite ingresar las temperaturas diarias de la semana.
        """
        print("Ingrese las temperaturas diarias de la semana:")
        for dia in range(1, 8):
            temp = float(input(f"Día {dia}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio semanal de temperatura.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)


def main():
    """
    Función principal del programa orientado a objetos.
    """
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()
