from producto import Producto
import os


class Inventario:
    """
    Maneja una lista de productos y su persistencia en archivo.
    Requisitos:
    - Añadir, eliminar, actualizar y buscar
    - Guardar automáticamente cambios en inventario.txt
    - Cargar inventario desde archivo al iniciar
    - Manejo robusto de excepciones de archivos
    """

    def __init__(self, ruta_archivo: str = "inventario.txt"):
        self.__productos = []
        self.__ruta = ruta_archivo

        # Al iniciar: cargar datos desde archivo (o crearlo si no existe)
        self.cargar_desde_archivo()

    # -------------------------
    # Lógica de negocio (POO)
    # -------------------------
    def id_existe(self, id_producto: str) -> bool:
        for p in self.__productos:
            if p.get_id() == id_producto:
                return True
        return False

    def anadir_producto(self, producto: Producto):
        """
        Retorna (ok: bool, mensaje: str)
        """
        if self.id_existe(producto.get_id()):
            return False, "Error: Ese ID ya existe. No se agregó."

        self.__productos.append(producto)

        ok_archivo, msg_archivo = self.guardar_en_archivo()
        if ok_archivo:
            return True, "Producto agregado y guardado en archivo correctamente."
        else:
            return False, f"Producto agregado en memoria, pero falló el guardado en archivo. Detalle: {msg_archivo}"

    def eliminar_por_id(self, id_producto: str):
        """
        Retorna (ok: bool, mensaje: str)
        """
        for i, p in enumerate(self.__productos):
            if p.get_id() == id_producto:
                self.__productos.pop(i)

                ok_archivo, msg_archivo = self.guardar_en_archivo()
                if ok_archivo:
                    return True, "Producto eliminado y archivo actualizado."
                else:
                    return False, f"Producto eliminado en memoria, pero falló la actualización del archivo. Detalle: {msg_archivo}"

        return False, "No se encontró un producto con ese ID."

    def actualizar_por_id(self, id_producto: str, nueva_cantidad=None, nuevo_precio=None):
        """
        Retorna (ok: bool, mensaje: str)
        """
        for p in self.__productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                ok_archivo, msg_archivo = self.guardar_en_archivo()
                if ok_archivo:
                    return True, "Producto actualizado y guardado en archivo."
                else:
                    return False, f"Producto actualizado en memoria, pero falló el guardado en archivo. Detalle: {msg_archivo}"

        return False, "No se encontró el ID para actualizar."

    def buscar_por_nombre(self, texto: str):
        texto = texto.strip().lower()
        resultados = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_todos(self):
        return self.__productos

    # -------------------------
    # Persistencia en archivos
    # -------------------------
    def asegurar_archivo(self):
        """
        Asegura que el archivo exista. Si no existe, lo crea.
        Maneja excepciones como PermissionError.
        Retorna (ok: bool, mensaje: str)
        """
        try:
            if not os.path.exists(self.__ruta):
                # Creamos un archivo vacío
                with open(self.__ruta, "w", encoding="utf-8") as f:
                    f.write("")
            return True, "Archivo listo."
        except PermissionError:
            return False, "PermissionError: No tienes permisos para crear/escribir el archivo."
        except OSError as e:
            return False, f"OSError: Error del sistema al asegurar el archivo. {e}"

    def cargar_desde_archivo(self):
        """
        Carga productos desde el archivo.
        - Si no existe, lo crea.
        - Si hay líneas corruptas, las ignora y continúa.
        Retorna (ok: bool, mensaje: str)
        """
        ok, msg = self.asegurar_archivo()
        if not ok:
            # No se puede ni crear el archivo: inventario queda vacío
            return False, msg

        try:
            self.__productos = []  # Reiniciamos en memoria
            lineas_corruptas = 0

            with open(self.__ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip() == "":
                        continue
                    try:
                        producto = Producto.desde_linea(linea)
                        # Evitar duplicados por seguridad
                        if not self.id_existe(producto.get_id()):
                            self.__productos.append(producto)
                    except ValueError:
                        lineas_corruptas += 1
                        # Se ignora la línea corrupta y se sigue

            if lineas_corruptas > 0:
                return True, f"Inventario cargado con advertencia: {lineas_corruptas} línea(s) corrupta(s) fueron ignoradas."
            return True, "Inventario cargado correctamente desde archivo."

        except FileNotFoundError:
            # Muy raro si asegurar_archivo funcionó, pero igual lo cubrimos
            return False, "FileNotFoundError: No se encontró el archivo del inventario."
        except PermissionError:
            return False, "PermissionError: No tienes permisos para leer el archivo."
        except OSError as e:
            return False, f"OSError: Error del sistema al leer el archivo. {e}"

    def guardar_en_archivo(self):
        """
        Guarda TODO el inventario en el archivo.
        Estrategia segura:
        - Escribe en un archivo temporal
        - Luego reemplaza el archivo real
        Retorna (ok: bool, mensaje: str)
        """
        ok, msg = self.asegurar_archivo()
        if not ok:
            return False, msg

        temp = self.__ruta + ".tmp"

        try:
            with open(temp, "w", encoding="utf-8") as f:
                for p in self.__productos:
                    f.write(p.to_linea() + "\n")

            # Reemplazo atómico (más seguro)
            os.replace(temp, self.__ruta)
            return True, "Archivo actualizado correctamente."

        except PermissionError:
            return False, "PermissionError: No tienes permisos para escribir en el archivo."
        except OSError as e:
            return False, f"OSError: Error del sistema al escribir el archivo. {e}"
        finally:
            # Limpieza: si quedó temp por error, intentamos borrarlo
            try:
                if os.path.exists(temp):
                    os.remove(temp)
            except Exception:
                pass