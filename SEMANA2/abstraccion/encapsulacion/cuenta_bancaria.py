"""
Ejemplo de ENCAPSULACIÓN en POO.

Encapsulación = ocultar los datos internos de un objeto y exponer
solo métodos controlados para modificarlos.
"""


class CuentaBancaria:
    def __init__(self, titular: str) -> None:
        self.titular = titular
        self.__saldo = 0.0  # Atributo "privado"

    def depositar(self, monto: float) -> None:
        """Aumenta el saldo si el monto es válido."""
        if monto <= 0:
            print("El monto a depositar debe ser positivo.")
            return
        self.__saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.__saldo:.2f}")

    def retirar(self, monto: float) -> None:
        """Disminuye el saldo si hay fondos suficientes."""
        if monto <= 0:
            print("El monto a retirar debe ser positivo.")
            return
        if monto > self.__saldo:
            print("Fondos insuficientes.")
            return
        self.__saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.__saldo:.2f}")

    def mostrar_saldo(self) -> float:
        """Devuelve el saldo actual (acceso controlado)."""
        return self.__saldo


if __name__ == "__main__":
    print("=== Ejemplo de ENCAPSULACIÓN ===")
    cuenta = CuentaBancaria("Bicker Rodríguez")
    cuenta.depositar(100)
    cuenta.retirar(30)
    print(f"Saldo final (acceso controlado): {cuenta.mostrar_saldo():.2f}")
