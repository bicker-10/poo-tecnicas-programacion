import json
from pathlib import Path
from inventario import Inventario

ARCHIVO_DEFAULT = "inventario.json"


def guardar_inventario(inventario: Inventario, ruta: str = ARCHIVO_DEFAULT) -> None:
    path = Path(ruta)
    with path.open("w", encoding="utf-8") as f:
        json.dump(inventario.to_dict(), f, ensure_ascii=False, indent=2)


def cargar_inventario(ruta: str = ARCHIVO_DEFAULT) -> Inventario:
    path = Path(ruta)
    if not path.exists():
        return Inventario()

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
        return Inventario.from_dict(data)