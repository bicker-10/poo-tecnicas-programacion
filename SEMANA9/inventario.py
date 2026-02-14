from producto import Producto


class Inventario:
    """
    Maneja una lista de productos.
    Requisitos:
    - Lista de productos
    - Añadir (ID único)
    - Eliminar por ID
    - Actualizar cantidad o precio por ID
    - Buscar por nombre (coincidencias parciales)
    - Mostrar todos
    """

    def __init__(self):
        self.__productos = []  # Lista de objetos Producto

    def id_existe(self, id_producto: str) -> bool:
        """Verifica si el ID ya está registrado."""
        for p in self.__productos:
            if p.get_id() == id_producto:
                return True
        return False

    def anadir_producto(self, producto: Producto) -> bool:
        """
        Añade un nuevo producto, asegurando ID único.
        Retorna True si se agregó, False si el ID ya existía.
        """
        if self.id_existe(producto.get_id()):
            return False
        self.__productos.append(producto)
        return True

    def eliminar_por_id(self, id_producto: str) -> bool:
        """
        Elimina un producto por su ID.
        Retorna True si se eliminó, False si no se encontró.
        """
        for i, p in enumerate(self.__productos):
            if p.get_id() == id_producto:
                self.__productos.pop(i)
                return True
        return False

    def actualizar_por_id(self, id_producto: str, nueva_cantidad=None, nuevo_precio=None) -> bool:
        """
        Actualiza cantidad y/o precio por ID.
        - Si nueva_cantidad no es None, actualiza cantidad.
        - Si nuevo_precio no es None, actualiza precio.
        Retorna True si se actualizó, False si no se encontró el ID.
        """
        for p in self.__productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return True
        return False

    def buscar_por_nombre(self, texto: str):
        """
        Busca productos por nombre usando coincidencia parcial (case-insensitive).
        Retorna una lista con coincidencias.
        """
        texto = texto.strip().lower()
        resultados = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_todos(self):
        """Retorna la lista completa de productos."""
        return self.__productos
