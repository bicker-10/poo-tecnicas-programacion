from producto import Producto
from inventario import Inventario
from storage import cargar_inventario, guardar_inventario, ARCHIVO_DEFAULT


def leer_int(mensaje: str, minimo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"Error: debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número entero válido.")


def leer_float(mensaje: str, minimo: float | None = None) -> float:
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"Error: debe ser >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número válido (ej. 12.50).")


def leer_texto(mensaje: str) -> str:
    while True:
        txt = input(mensaje).strip()
        if txt:
            return txt
        print("Error: no puede estar vacío.")


def mostrar_producto(p: Producto) -> None:
    print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")


def menu() -> None:
    print("\n=== SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO ===")
    print("1) Añadir producto")
    print("2) Eliminar producto por ID")
    print("3) Actualizar cantidad o precio")
    print("4) Buscar productos por nombre")
    print("5) Mostrar todos los productos")
    print("6) Mostrar resumen del inventario")
    print("7) Guardar inventario")
    print("0) Salir")


def main() -> None:
    inventario: Inventario = cargar_inventario(ARCHIVO_DEFAULT)
    print(f"Inventario cargado desde '{ARCHIVO_DEFAULT}'.")

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                pid = leer_texto("ID (único): ")
                nombre = leer_texto("Nombre: ")
                cantidad = leer_int("Cantidad (>=0): ", minimo=0)
                precio = leer_float("Precio (>=0): ", minimo=0.0)

                inventario.agregar_producto(Producto(pid, nombre, cantidad, precio))
                print("Producto agregado correctamente.")

            elif opcion == "2":
                pid = leer_texto("Ingrese el ID a eliminar: ")
                inventario.eliminar_producto(pid)
                print("Producto eliminado.")

            elif opcion == "3":
                pid = leer_texto("Ingrese el ID a actualizar: ")
                prod = inventario.obtener_producto(pid)
                if not prod:
                    print("No existe un producto con ese ID.")
                    continue

                print("Producto actual:")
                mostrar_producto(prod)

                print("¿Qué desea actualizar?")
                print("1) Cantidad")
                print("2) Precio")
                print("3) Ambos")
                sub = input("Opción: ").strip()

                if sub == "1":
                    nueva_cant = leer_int("Nueva cantidad (>=0): ", minimo=0)
                    inventario.actualizar_producto(pid, nueva_cantidad=nueva_cant)
                elif sub == "2":
                    nuevo_precio = leer_float("Nuevo precio (>=0): ", minimo=0.0)
                    inventario.actualizar_producto(pid, nuevo_precio=nuevo_precio)
                elif sub == "3":
                    nueva_cant = leer_int("Nueva cantidad (>=0): ", minimo=0)
                    nuevo_precio = leer_float("Nuevo precio (>=0): ", minimo=0.0)
                    inventario.actualizar_producto(pid, nueva_cantidad=nueva_cant, nuevo_precio=nuevo_precio)
                else:
                    print("Opción inválida.")
                    continue

                print("Producto actualizado correctamente.")

            elif opcion == "4":
                nombre = leer_texto("Ingrese nombre o parte del nombre: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if not resultados:
                    print("No se encontraron productos.")
                else:
                    print(f"Se encontraron {len(resultados)} producto(s):")
                    for p in resultados:
                        mostrar_producto(p)

            elif opcion == "5":
                productos = inventario.listar_todos()
                if not productos:
                    print("Inventario vacío.")
                else:
                    print("\n--- LISTA DE PRODUCTOS ---")
                    for p in productos:
                        mostrar_producto(p)

            elif opcion == "6":
                distintos, unidades, valor = inventario.resumen_inventario()
                print("\n--- RESUMEN ---")
                print(f"Productos distintos: {distintos}")
                print(f"Unidades totales: {unidades}")
                print(f"Valor total inventario: ${valor:.2f}")

            elif opcion == "7":
                guardar_inventario(inventario, ARCHIVO_DEFAULT)
                print(f"Inventario guardado en '{ARCHIVO_DEFAULT}'.")

            elif opcion == "0":
                # Guardado automático antes de salir (buena práctica)
                guardar_inventario(inventario, ARCHIVO_DEFAULT)
                print("Inventario guardado. Saliendo…")
                break

            else:
                print("Opción inválida. Intente de nuevo.")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()