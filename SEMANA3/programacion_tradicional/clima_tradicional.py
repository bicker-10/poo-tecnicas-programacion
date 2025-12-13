"""
Programa en Programación Tradicional para calcular
el promedio semanal del clima.
Se utilizan funciones y estructuras básicas.
"""

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de la semana
    y las almacena en una lista.
    """
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana:")
    for dia in range(1, 8):
        temp = float(input(f"Día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal a partir de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal del programa tradicional.
    """
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()
