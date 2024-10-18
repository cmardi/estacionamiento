

# Un estacionamiento está buscando una manera de automatizar la gestión de los vehículos
# que ingresan, asegurando un control adecuado del tipo de vehículo, el tiempo de
# permanencia y los pagos correspondientes. El sistema debe poder registrar diferentes
# tipos de vehículos, calcular las tarifas y generar un resumen para el cliente.
# Tu equipo ha sido asignado para desarrollar la estructura básica de este sistema, que
# permita gestionar vehículos y calcular tarifas en función del tipo de vehículo y del
# tiempo que permanecen en el estacionamiento.





from dataclasses import dataclass
from typing import List

# Excepciones personalizadas
class TiempoInvalidoError(Exception):
    """Se lanza cuando el tiempo de permanencia es negativo o no válido."""
    pass

class VehiculoNoEncontradoError(Exception):
    """Se lanza cuando se intenta calcular la tarifa de un vehículo no registrado."""
    pass

@dataclass
class Vehiculo:
    """Clase base para todos los vehículos."""
    placa: str
    marca: str

    def __str__(self) -> str:
        return f"{self.marca}, Placa: {self.placa}"

class Automovil(Vehiculo):
    """Clase que representa un automóvil."""
    def __init__(self, placa: str, marca: str, tarifa_por_hora: float = 2):
        super().__init__(placa, marca)
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_tarifa(self, tiempo: float) -> float:
        return self.tarifa_por_hora * tiempo

class Motocicleta(Vehiculo):
    """Clase que representa una motocicleta."""
    def __init__(self, placa: str, marca: str, tarifa_por_hora: float = 1):
        super().__init__(placa, marca)
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_tarifa(self, tiempo: float) -> float:
        return self.tarifa_por_hora * tiempo

class ControlDeTiempo(Automovil, Motocicleta):
    """Clase para controlar el tiempo de permanencia."""
    def validar_tiempo(self, tiempo: float) -> bool:
        if tiempo <= 0:
            raise TiempoInvalidoError("El tiempo debe ser un valor positivo")
        return True

class Estacionamiento:
    """Clase para gestionar el estacionamiento."""
    def __init__(self):
        self.vehiculos: List[Vehiculo] = []

    def registrar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)

    def calcular_tarifa(self, vehiculo: Vehiculo, tiempo: float) -> float:
        if vehiculo not in self.vehiculos:
            raise VehiculoNoEncontradoError("El vehículo no está registrado en el estacionamiento")
        
        control_tiempo = ControlDeTiempo(vehiculo.placa, vehiculo.marca)
        control_tiempo.validar_tiempo(tiempo)
        
        return vehiculo.calcular_tarifa(tiempo)

@dataclass
class Recibo:
    """Clase para generar recibos."""
    vehiculo: Vehiculo
    tiempo: float
    total: float

    def __str__(self) -> str:
        return f"""Recibo:
Vehículo: {self.vehiculo}
Tiempo: {self.tiempo} horas
Total a pagar: ${self.total}"""

# Ejemplo de uso
def main():
    try:
        # Crear instancia de Automóvil
        auto = Automovil(placa="ABC123", marca="Toyota", tarifa_por_hora=2)
        
        # Registrar automóvil en el estacionamiento
        estacionamiento = Estacionamiento()
        estacionamiento.registrar_vehiculo(auto)
        
        # Calcular tarifa para un tiempo válido
        tiempo = 3  # Horas
        tarifa = estacionamiento.calcular_tarifa(auto, tiempo)
        print(f"Tarifa calculada: {tarifa}")
        
        # Generar recibo
        recibo = Recibo(vehiculo=auto, tiempo=tiempo, total=tarifa)
        print(recibo)
        
        # Ejemplo con motocicleta
        moto = Motocicleta(placa="XYZ789", marca="Honda")
        estacionamiento.registrar_vehiculo(moto)
        tarifa_moto = estacionamiento.calcular_tarifa(moto, 2)
        recibo_moto = Recibo(vehiculo=moto, tiempo=2, total=tarifa_moto)
        print("\n", recibo_moto)

    except TiempoInvalidoError as e:
        print(f"Error: {e}")
    except VehiculoNoEncontradoError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()