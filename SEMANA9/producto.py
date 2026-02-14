class Producto:
    """
    Representa un producto dentro del inventario.
    Requisitos:
    - Atributos: id (único), nombre, cantidad, precio
    - Métodos: constructor, getters y setters
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ---- Getters ----
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # ---- Setters ----
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_cantidad(self, cantidad: int):
        self.__cantidad = cantidad

    def set_precio(self, precio: float):
        self.__precio = precio

    def __str__(self) -> str:
        # Formato claro para mostrar en consola
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
