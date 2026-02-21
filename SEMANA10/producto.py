class Producto:
    """
    Representa un producto dentro del inventario.
    Requisitos:
    - Atributos: id (único), nombre, cantidad, precio
    - Métodos: constructor, getters y setters
    - Soporte para serializar/deserializar a texto (archivo)
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

    # ---- Archivo: CSV simple ----
    def to_linea(self) -> str:
        """
        Convierte el producto a una línea de texto para guardar en archivo.
        Formato: id|nombre|cantidad|precio
        Usamos '|' para evitar problemas si el nombre tiene comas.
        """
        return f"{self.__id}|{self.__nombre}|{self.__cantidad}|{self.__precio}"

    @staticmethod
    def desde_linea(linea: str):
        """
        Reconstruye un Producto desde una línea del archivo.
        Lanza ValueError si la línea está corrupta.
        """
        partes = linea.strip().split("|")
        if len(partes) != 4:
            raise ValueError("Formato inválido (se esperaban 4 campos).")

        id_producto = partes[0].strip()
        nombre = partes[1].strip()
        cantidad = int(partes[2].strip())
        precio = float(partes[3].strip())

        if not id_producto or not nombre:
            raise ValueError("ID o nombre vacío.")

        if cantidad < 0 or precio < 0:
            raise ValueError("Cantidad o precio negativo.")

        return Producto(id_producto, nombre, cantidad, precio)

    def __str__(self) -> str:
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"