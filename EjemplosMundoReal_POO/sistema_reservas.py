"""
Ejemplo del mundo real: Sistema de Reservas de Hotel (POO)

- Modela clientes, habitaciones, reservas y un hotel.
- Demuestra interacción entre objetos:
  Hotel crea reservas, valida disponibilidad y guarda el historial.
- Incluye encapsulamiento (atributos "privados" con _).
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Cliente:
    """Representa a un cliente del hotel."""
    nombre: str
    cedula: str


@dataclass(frozen=True)
class Habitacion:
    """Representa una habitación disponible para reservar."""
    numero: int
    tipo: str  # Ej: "Simple", "Doble", "Suite"
    precio_por_noche: float


@dataclass
class Reserva:
    """Relaciona un Cliente con una Habitacion y un rango de fechas."""
    cliente: Cliente
    habitacion: Habitacion
    fecha_entrada: date
    fecha_salida: date

    def noches(self) -> int:
        """Calcula el número de noches de la reserva."""
        return (self.fecha_salida - self.fecha_entrada).days

    def costo_total(self) -> float:
        """Calcula el costo total de la reserva."""
        return self.noches() * self.habitacion.precio_por_noche

    def se_superpone(self, otra: "Reserva") -> bool:
        """
        Verifica si dos reservas se superponen (misma habitación y fechas que se cruzan).
        Regla: [entrada, salida) para evitar conflicto el mismo día de salida/entrada.
        """
        if self.habitacion.numero != otra.habitacion.numero:
            return False
        return not (self.fecha_salida <= otra.fecha_entrada or self.fecha_entrada >= otra.fecha_salida)


class Hotel:
    """
    Clase principal que gestiona habitaciones y reservas.
    Encapsula la lista de reservas y controla la disponibilidad.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self._habitaciones: list[Habitacion] = []
        self._reservas: list[Reserva] = []

    def agregar_habitacion(self, habitacion: Habitacion) -> None:
        """Agrega una habitación al hotel."""
        self._habitaciones.append(habitacion)

    def listar_habitaciones(self) -> None:
        """Muestra habitaciones registradas."""
        print(f"\nHabitaciones de {self.nombre}:")
        for h in self._habitaciones:
            print(f"- #{h.numero} | {h.tipo} | ${h.precio_por_noche:.2f}/noche")

    def esta_disponible(self, habitacion: Habitacion, entrada: date, salida: date) -> bool:
        """Verifica si una habitación está disponible en el rango de fechas."""
        reserva_propuesta = Reserva(Cliente("TEMP", "000"), habitacion, entrada, salida)
        for r in self._reservas:
            if reserva_propuesta.se_superpone(r):
                return False
        return True

    def crear_reserva(self, cliente: Cliente, numero_habitacion: int, entrada: date, salida: date) -> Reserva | None:
        """
        Crea una reserva si la habitación existe y está disponible.
        Retorna la reserva creada o None si no se puede reservar.
        """
        if salida <= entrada:
            print("❌ Error: La fecha de salida debe ser posterior a la fecha de entrada.")
            return None

        habitacion = next((h for h in self._habitaciones if h.numero == numero_habitacion), None)
        if habitacion is None:
            print("❌ Error: No existe esa habitación.")
            return None

        if not self.esta_disponible(habitacion, entrada, salida):
            print("❌ No disponible: esa habitación ya está reservada en esas fechas.")
            return None

        reserva = Reserva(cliente, habitacion, entrada, salida)
        self._reservas.append(reserva)
        print("✅ Reserva creada con éxito.")
        return reserva

    def mostrar_reservas(self) -> None:
        """Imprime todas las reservas registradas."""
        print(f"\nReservas en {self.nombre}:")
        if not self._reservas:
            print("- (Sin reservas)")
            return

        for r in self._reservas:
            print(
                f"- {r.cliente.nombre} | Hab #{r.habitacion.numero} ({r.habitacion.tipo}) "
                f"| {r.fecha_entrada} -> {r.fecha_salida} | {r.noches()} noches | Total: ${r.costo_total():.2f}"
            )


def main():
    # --- Creación de objetos (mundo real) ---
    hotel = Hotel("Hotel Amazonía")
    hotel.agregar_habitacion(Habitacion(101, "Simple", 25.0))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 35.0))
    hotel.agregar_habitacion(Habitacion(201, "Suite", 60.0))

    cliente1 = Cliente("Bicker Rodríguez", "0102030405")
    cliente2 = Cliente("Kerly Pérez", "0911223344")

    hotel.listar_habitaciones()

    # --- Interacción entre objetos (reservas) ---
    hotel.crear_reserva(cliente1, 101, date(2025, 12, 1), date(2025, 12, 5))
    hotel.crear_reserva(cliente2, 101, date(2025, 12, 3), date(2025, 12, 6))  # debe fallar por superposición
    hotel.crear_reserva(cliente2, 102, date(2025, 12, 3), date(2025, 12, 6))  # debe funcionar

    hotel.mostrar_reservas()


if __name__ == "__main__":
    main()
