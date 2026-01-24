# ------------------------------------------------------------
# Programa: Sistema simple de compras con constructor y destructor
# Autor: Bicker
# Descripción:
#   Demuestra el uso de __init__ (constructor) para inicializar
#   objetos y abrir un recurso (archivo de log), y __del__
#   (destructor) para liberar/limpiar ese recurso (cerrar archivo).
# ------------------------------------------------------------

from datetime import datetime


class Producto:
    """
    Clase Producto:
    - __init__: inicializa nombre y precio (atributos del objeto)
    - __del__: muestra un mensaje cuando el objeto se elimina (demostrativo)
    """

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

    def __del__(self):
        # Nota: este mensaje puede no verse siempre, depende del recolector de basura.
        # Se incluye para demostrar el uso del destructor.
        # Evita hacer lógica crítica aquí.
        pass


class CarritoCompras:
    """
    Clase CarritoCompras:
    - __init__: inicializa cliente, lista de productos y abre un archivo de log.
    - __del__: se encarga de cerrar el archivo si quedó abierto (limpieza).
    """

    def __init__(self, cliente: str, archivo_log: str = "compras_log.txt"):
        self.cliente = cliente
        self.productos = []  # lista (tipo de dato compuesto)
        self.archivo_log = archivo_log

        # Recurso: archivo abierto (ejemplo de "limpieza" aplicable)
        self._log = open(self.archivo_log, "a", encoding="utf-8")

        self._escribir_log(f"Se creó un carrito para el cliente: {self.cliente}")

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        self._escribir_log(f"Producto agregado: {producto.nombre} (${producto.precio:.2f})")

    def total(self) -> float:
        return sum(p.precio for p in self.productos)

    def mostrar_resumen(self):
        print("\n--- RESUMEN DE COMPRA ---")
        print(f"Cliente: {self.cliente}")
        print("Productos:")
        for p in self.productos:
            print(f" - {p}")
        print(f"Total: ${self.total():.2f}")
        print("------------------------\n")

    def _escribir_log(self, mensaje: str):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._log.write(f"[{fecha_hora}] {mensaje}\n")
        self._log.flush()

    def cerrar(self):
        """
        Buena práctica: cerrar recursos manualmente cuando ya no se necesitan.
        Esto NO reemplaza a __del__, pero lo complementa.
        """
        if hasattr(self, "_log") and self._log and not self._log.closed:
            self._escribir_log("Cierre manual del archivo de log (método cerrar()).")
            self._log.close()

    def __del__(self):
        """
        Destructor:
        Intenta cerrar el archivo de log si todavía está abierto.
        Importante: __del__ no garantiza ejecución inmediata.
        """
        try:
            if hasattr(self, "_log") and self._log and not self._log.closed:
                self._escribir_log("Cierre automático del archivo de log (__del__).")
                self._log.close()
        except Exception:
            # Evitar que errores en __del__ rompan el cierre del programa
            pass


def main():
    # Tipos de datos usados:
    # - str: cliente
    # - float: precios
    # - list: productos
    # - bool: control de ejecución
    cliente = "Bicker"
    continuar = True  # boolean

    carrito = CarritoCompras(cliente)

    while continuar:
        print("1) Agregar producto")
        print("2) Ver resumen")
        print("3) Finalizar compra")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            precio_texto = input("Precio del producto (ej: 2.50): ").strip()

            try:
                precio = float(precio_texto)
                producto = Producto(nombre, precio)
                carrito.agregar_producto(producto)
                print("✅ Producto agregado.\n")
            except ValueError:
                print("❌ Precio inválido. Ingresa un número (ej: 2.50).\n")

        elif opcion == "2":
            carrito.mostrar_resumen()

        elif opcion == "3":
            carrito.mostrar_resumen()
            print("Compra finalizada. Gracias.")
            continuar = False

        else:
            print("❌ Opción inválida.\n")

    # Cierre manual recomendado
    carrito.cerrar()

    # Al terminar main, el programa puede liberar objetos.
    # __del__ podría ejecutarse aquí o después (no es 100% inmediato).


if __name__ == "__main__":
    main()
