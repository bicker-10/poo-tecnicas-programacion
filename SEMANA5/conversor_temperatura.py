"""
Programa: Conversor de Temperatura
Descripción:
Este programa convierte una temperatura ingresada en grados Celsius
a grados Fahrenheit. Utiliza distintos tipos de datos y
buenas prácticas de identificación en Python.
"""

def convertir_celsius_a_fahrenheit(temperatura_celsius):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    return temperatura_fahrenheit


# Entrada de datos
nombre_usuario = input("Ingrese su nombre: ")        # string
temperatura_celsius = float(input("Ingrese la temperatura en °C: "))  # float

# Proceso
temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

# Evaluación booleana
es_temperatura_alta = temperatura_fahrenheit > 86     # boolean

# Salida de resultados
print("\n--- RESULTADOS ---")
print(f"Usuario: {nombre_usuario}")
print(f"Temperatura en Celsius: {temperatura_celsius} °C")
print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit} °F")

if es_temperatura_alta:
    print("La temperatura es considerada ALTA.")
else:
    print("La temperatura es considerada NORMAL.")
