from producto import Producto
from inventario import Inventario


def leer_entero(mensaje: str) -> int:
    """Lee un entero validando entrada."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("⚠ Error: el valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠ Error: ingresa un número entero válido.")


def leer_flotante(mensaje: str) -> float:
    """Lee un flotante validando entrada."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("⚠ Error: el valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠ Error: ingresa un número válido (ej. 10.50).")


def menu():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 50)
        print("📦 SISTEMA DE GESTIÓN DE INVENTARIOS")
        print("=" * 50)
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("0. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n➕ AÑADIR PRODUCTO")
            id_producto = input("ID (único): ").strip()

            if inventario.id_existe(id_producto):
                print("❌ Error: Ese ID ya existe. No se agregó el producto.")
                continue

            nombre = input("Nombre: ").strip()
            cantidad = leer_entero("Cantidad: ")
            precio = leer_flotante("Precio: ")

            producto = Producto(id_producto, nombre, cantidad, precio)
            if inventario.anadir_producto(producto):
                print("✅ Producto agregado correctamente.")
            else:
                print("❌ No se pudo agregar (ID duplicado).")

        elif opcion == "2":
            print("\n🗑 ELIMINAR PRODUCTO")
            id_producto = input("Ingresa el ID a eliminar: ").strip()
            if inventario.eliminar_por_id(id_producto):
                print("✅ Producto eliminado.")
            else:
                print("❌ No se encontró un producto con ese ID.")

        elif opcion == "3":
            print("\n✏ ACTUALIZAR PRODUCTO")
            id_producto = input("Ingresa el ID a actualizar: ").strip()

            if not inventario.id_existe(id_producto):
                print("❌ No existe un producto con ese ID.")
                continue

            print("¿Qué deseas actualizar?")
            print("1. Cantidad")
            print("2. Precio")
            print("3. Cantidad y Precio")
            subop = input("Opción: ").strip()

            nueva_cantidad = None
            nuevo_precio = None

            if subop == "1":
                nueva_cantidad = leer_entero("Nueva cantidad: ")
            elif subop == "2":
                nuevo_precio = leer_flotante("Nuevo precio: ")
            elif subop == "3":
                nueva_cantidad = leer_entero("Nueva cantidad: ")
                nuevo_precio = leer_flotante("Nuevo precio: ")
            else:
                print("❌ Opción inválida.")
                continue

            if inventario.actualizar_por_id(id_producto, nueva_cantidad, nuevo_precio):
                print("✅ Producto actualizado correctamente.")
            else:
                print("❌ No se pudo actualizar (ID no encontrado).")

        elif opcion == "4":
            print("\n🔎 BUSCAR POR NOMBRE")
            texto = input("Ingresa el nombre o parte del nombre: ")
            resultados = inventario.buscar_por_nombre(texto)

            if len(resultados) == 0:
                print("❌ No se encontraron productos con ese criterio.")
            else:
                print(f"✅ Coincidencias encontradas: {len(resultados)}")
                for p in resultados:
                    print(" -", p)

        elif opcion == "5":
            print("\n📋 LISTA DE PRODUCTOS")
            productos = inventario.mostrar_todos()

            if len(productos) == 0:
                print("📭 Inventario vacío.")
            else:
                for p in productos:
                    print(" -", p)

        elif opcion == "0":
            print("\n👋 Saliendo del sistema. ¡Buen trabajo!")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
