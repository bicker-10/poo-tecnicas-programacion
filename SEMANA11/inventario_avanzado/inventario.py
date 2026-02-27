from __future__ import annotations
from typing import Dict, List, Optional, Tuple, Set
from producto import Producto


class Inventario:
    """
    Inventario basado en diccionario para búsqueda rápida:
      productos: Dict[str, Producto]  -> clave = ID único
    Además usamos:
      - set para indexar nombres normalizados
      - list para ordenar resultados al mostrar
      - tuple para devolver resúmenes inmutables
    """

    def __init__(self) -> None:
        self.productos: Dict[str, Producto] = {}
        self._nombres_index: Set[str] = set()

    @staticmethod
    def _norm(texto: str) -> str:
        return texto.strip().lower()

    def _reconstruir_index(self) -> None:
        self._nombres_index = {self._norm(p.nombre) for p in self.productos.values()}

    def agregar_producto(self, producto: Producto) -> None:
        pid = producto.get_id().strip()
        if pid in self.productos:
            raise ValueError(f"Ya existe un producto con ID '{pid}'.")
        self.productos[pid] = producto
        self._nombres_index.add(self._norm(producto.get_nombre()))

    def eliminar_producto(self, producto_id: str) -> None:
        pid = producto_id.strip()
        if pid not in self.productos:
            raise KeyError(f"No existe producto con ID '{pid}'.")
        eliminado = self.productos.pop(pid)
        # Reindex: forma segura cuando quitamos un elemento
        self._reconstruir_index()

    def actualizar_producto(
        self,
        producto_id: str,
        nueva_cantidad: Optional[int] = None,
        nuevo_precio: Optional[float] = None,
    ) -> None:
        pid = producto_id.strip()
        if pid not in self.productos:
            raise KeyError(f"No existe producto con ID '{pid}'.")
        producto = self.productos[pid]

        if nueva_cantidad is not None:
            producto.set_cantidad(int(nueva_cantidad))
        if nuevo_precio is not None:
            producto.set_precio(float(nuevo_precio))

    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """
        Búsqueda por coincidencia parcial (contiene).
        Retorna lista de productos encontrados.
        """
        consulta = self._norm(nombre)
        if not consulta:
            return []

        # Si la consulta exacta NO está en el set, igual podemos buscar parcial.
        resultados = [
            p for p in self.productos.values()
            if consulta in self._norm(p.get_nombre())
        ]

        # Orden alfabético por nombre
        resultados.sort(key=lambda p: self._norm(p.get_nombre()))
        return resultados

    def listar_todos(self) -> List[Producto]:
        productos_lista = list(self.productos.values())
        productos_lista.sort(key=lambda p: (self._norm(p.get_nombre()), p.get_id()))
        return productos_lista

    def obtener_producto(self, producto_id: str) -> Optional[Producto]:
        return self.productos.get(producto_id.strip())

    def resumen_inventario(self) -> Tuple[int, int, float]:
        """
        Retorna una tupla (inmutable) con:
        (cantidad_de_productos_distintos, unidades_totales, valor_total)
        """
        distintos = len(self.productos)
        unidades = sum(p.get_cantidad() for p in self.productos.values())
        valor = sum(p.get_cantidad() * p.get_precio() for p in self.productos.values())
        return (distintos, unidades, round(valor, 2))

    def to_dict(self) -> dict:
        return {
            "productos": [p.to_dict() for p in self.productos.values()]
        }

    @staticmethod
    def from_dict(data: dict) -> "Inventario":
        inv = Inventario()
        for item in data.get("productos", []):
            prod = Producto.from_dict(item)
            inv.productos[prod.get_id()] = prod
        inv._reconstruir_index()
        return inv