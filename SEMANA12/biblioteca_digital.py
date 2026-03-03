from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Set, Optional


# =========================
#        MODELOS
# =========================

@dataclass
class Libro:
    """
    Representa un libro de la biblioteca.
    Requisito clave:
    - Autor y título se guardan en una TUPLA porque no deben cambiar (inmutables).
    """
    autor_titulo: tuple[str, str]   # (autor, titulo) -> inmutable por diseño
    categoria: str
    isbn: str

    @property
    def autor(self) -> str:
        return self.autor_titulo[0]

    @property
    def titulo(self) -> str:
        return self.autor_titulo[1]

    def __str__(self) -> str:
        return f"'{self.titulo}' - {self.autor} | Cat: {self.categoria} | ISBN: {self.isbn}"


class Usuario:
    """
    Representa un usuario.
    - ID único
    - Lista de libros actualmente prestados (LISTA).
    """
    def __init__(self, nombre: str, user_id: str) -> None:
        self.nombre: str = nombre
        self.user_id: str = user_id
        self.libros_prestados: List[Libro] = []  # lista por requisito

    def __str__(self) -> str:
        return f"{self.nombre} (ID: {self.user_id})"


# =========================
#      GESTIÓN CENTRAL
# =========================

class Biblioteca:
    """
    Gestiona:
    - Libros disponibles: DICCIONARIO {isbn: Libro} (búsqueda rápida por clave)
    - Usuarios: DICCIONARIO {id: Usuario} para acceder rápido al objeto
    - IDs únicos: CONJUNTO set() para asegurar unicidad
    - Préstamos: registro simple por usuario (la lista dentro del Usuario)
    """
    def __init__(self) -> None:
        self.libros_disponibles: Dict[str, Libro] = {}  # isbn -> Libro
        self.usuarios: Dict[str, Usuario] = {}          # user_id -> Usuario
        self.ids_usuarios: Set[str] = set()             # unicidad

    # -------- Libros --------

    def agregar_libro(self, libro: Libro) -> bool:
        """
        Añade un libro al catálogo (disponible).
        Retorna True si se agregó, False si ya existía el ISBN.
        """
        if libro.isbn in self.libros_disponibles:
            return False
        self.libros_disponibles[libro.isbn] = libro
        return True

    def quitar_libro(self, isbn: str) -> bool:
        """
        Quita un libro del catálogo disponible.
        No controla si está prestado porque los prestados NO están en 'libros_disponibles'.
        """
        if isbn not in self.libros_disponibles:
            return False
        del self.libros_disponibles[isbn]
        return True

    # -------- Usuarios --------

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra usuario si su ID es único (conjunto).
        """
        if usuario.user_id in self.ids_usuarios:
            return False
        self.ids_usuarios.add(usuario.user_id)
        self.usuarios[usuario.user_id] = usuario
        return True

    def dar_de_baja_usuario(self, user_id: str) -> bool:
        """
        Da de baja a un usuario.
        Regla razonable: no permitimos baja si tiene libros prestados.
        """
        usuario = self.usuarios.get(user_id)
        if usuario is None:
            return False

        if usuario.libros_prestados:
            # Evitamos "desaparecer" un usuario con préstamos activos.
            return False

        del self.usuarios[user_id]
        self.ids_usuarios.remove(user_id)
        return True

    # -------- Préstamos --------

    def prestar_libro(self, user_id: str, isbn: str) -> bool:
        """
        Presta un libro:
        - Verifica usuario existente
        - Verifica libro disponible
        - Lo mueve: disponibles -> lista prestados del usuario
        """
        usuario = self.usuarios.get(user_id)
        if usuario is None:
            return False

        libro = self.libros_disponibles.get(isbn)
        if libro is None:
            return False

        # Quitar de disponibles y agregar a la lista del usuario
        del self.libros_disponibles[isbn]
        usuario.libros_prestados.append(libro)
        return True

    def devolver_libro(self, user_id: str, isbn: str) -> bool:
        """
        Devuelve un libro:
        - Verifica usuario
        - Busca el libro en su lista prestada
        - Lo mueve de vuelta a disponibles
        """
        usuario = self.usuarios.get(user_id)
        if usuario is None:
            return False

        for i, libro in enumerate(usuario.libros_prestados):
            if libro.isbn == isbn:
                # Quitar de prestados y volver a disponibles
                usuario.libros_prestados.pop(i)
                self.libros_disponibles[isbn] = libro
                return True

        return False  # no lo tenía prestado

    # -------- Búsquedas --------

    def buscar_por_titulo(self, titulo: str) -> List[Libro]:
        """
        Busca por título (coincidencia parcial, no sensible a mayúsculas).
        Busca en disponibles y también en prestados (para un catálogo total).
        """
        titulo = titulo.strip().lower()
        resultados: List[Libro] = []

        for libro in self._todos_los_libros():
            if titulo in libro.titulo.lower():
                resultados.append(libro)

        return resultados

    def buscar_por_autor(self, autor: str) -> List[Libro]:
        autor = autor.strip().lower()
        resultados: List[Libro] = []

        for libro in self._todos_los_libros():
            if autor in libro.autor.lower():
                resultados.append(libro)

        return resultados

    def buscar_por_categoria(self, categoria: str) -> List[Libro]:
        categoria = categoria.strip().lower()
        resultados: List[Libro] = []

        for libro in self._todos_los_libros():
            if categoria == libro.categoria.lower():
                resultados.append(libro)

        return resultados

    def listar_libros_prestados(self, user_id: str) -> Optional[List[Libro]]:
        """
        Devuelve la lista de libros prestados del usuario.
        Retorna None si el usuario no existe.
        """
        usuario = self.usuarios.get(user_id)
        if usuario is None:
            return None
        return list(usuario.libros_prestados)  # copia

    # -------- Utilidad interna --------

    def _todos_los_libros(self) -> List[Libro]:
        """
        Devuelve todos los libros: disponibles + prestados.
        """
        libros: List[Libro] = list(self.libros_disponibles.values())
        for u in self.usuarios.values():
            libros.extend(u.libros_prestados)
        return libros

    # -------- Reportes simples --------

    def mostrar_catalogo_disponible(self) -> None:
        print("\n=== Catálogo (Disponibles) ===")
        if not self.libros_disponibles:
            print("No hay libros disponibles.")
            return
        for libro in self.libros_disponibles.values():
            print("-", libro)

    def mostrar_usuarios(self) -> None:
        print("\n=== Usuarios registrados ===")
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for u in self.usuarios.values():
            print("-", u)


# =========================
#         PRUEBAS
# =========================

def main() -> None:
    biblio = Biblioteca()

    # Crear libros (autor, titulo) en TUPLA -> inmutable
    l1 = Libro(("Gabriel García Márquez", "Cien años de soledad"), "Novela", "978-0307474728")
    l2 = Libro(("George Orwell", "1984"), "Distopía", "978-0451524935")
    l3 = Libro(("Yuval Noah Harari", "Sapiens"), "Historia", "978-0062316097")

    # Agregar libros
    print("Agregar libros:")
    print("l1:", biblio.agregar_libro(l1))
    print("l2:", biblio.agregar_libro(l2))
    print("l3:", biblio.agregar_libro(l3))
    print("l3 repetido:", biblio.agregar_libro(l3))  # False por ISBN repetido

    biblio.mostrar_catalogo_disponible()

    # Registrar usuarios (ID único con SET)
    u1 = Usuario("Ana Pérez", "U001")
    u2 = Usuario("Carlos Ruiz", "U002")

    print("\nRegistrar usuarios:")
    print("u1:", biblio.registrar_usuario(u1))
    print("u2:", biblio.registrar_usuario(u2))
    print("u1 repetido:", biblio.registrar_usuario(Usuario("Ana 2", "U001")))  # False

    biblio.mostrar_usuarios()

    # Prestar y devolver
    print("\nPréstamos:")
    print("Prestar l2 a U001:", biblio.prestar_libro("U001", "978-0451524935"))
    print("Prestar l2 otra vez (ya no está):", biblio.prestar_libro("U002", "978-0451524935"))
    print("Prestar l1 a U001:", biblio.prestar_libro("U001", "978-0307474728"))

    biblio.mostrar_catalogo_disponible()

    print("\nLibros prestados a U001:")
    prestados = biblio.listar_libros_prestados("U001")
    for libro in prestados or []:
        print("-", libro)

    print("\nDevolver l2 de U001:", biblio.devolver_libro("U001", "978-0451524935"))
    biblio.mostrar_catalogo_disponible()

    # Búsquedas
    print("\nBúsqueda por título 'sapiens':")
    for libro in biblio.buscar_por_titulo("sapiens"):
        print("-", libro)

    print("\nBúsqueda por autor 'orwell':")
    for libro in biblio.buscar_por_autor("orwell"):
        print("-", libro)

    print("\nBúsqueda por categoría 'novela':")
    for libro in biblio.buscar_por_categoria("Novela"):
        print("-", libro)

    # Baja de usuario (bloqueada si tiene préstamos)
    print("\nDar de baja U001 (tiene préstamos):", biblio.dar_de_baja_usuario("U001"))

    # Devolver todo y dar de baja
    print("Devolver l1 de U001:", biblio.devolver_libro("U001", "978-0307474728"))
    print("Dar de baja U001 (ya sin préstamos):", biblio.dar_de_baja_usuario("U001"))
    biblio.mostrar_usuarios()


if __name__ == "__main__":
    main()