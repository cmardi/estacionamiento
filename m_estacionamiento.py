from dataclasses import dataclass

@dataclass
class Vehiculo:
    placa : str
    marca: str

    def __str__(self) -> str:
        return f"Placa: {self.placa}, Marca: {self.marca}"

class Automovil(Vehiculo):
    def __init__(self, placa, marca, tarifahora):
        super().__init__(placa, marca)
        self.tarifahora = tarifahora

    def calcular_tarifa(self, tiempo):
        total = self.tarifahora * tiempo
        return total

class Motocicleta(Vehiculo):
    def __init__(self, placa, marca, tarifahora):
        super().__init__(placa, marca)
        self.tarifahora = tarifahora
        self.tarifahora = 1

    def calcular_tarifa(self,tiempo):
        total = self.tarifahora * tiempo
        return total


class Estacionamiento():
    def __init__(self):
        self.vehiculos = []

    def registro_vehiculos(self, nuevovehiculo):
        self.vehiculos.append(nuevovehiculo)
        return f"{nuevovehiculo}, Ingresado"

# est = Estacionamiento()
# a1 = est.registro_vehiculos(5)
# print(a1)
    def calcular_tarifa (self, vehiculo: Vehiculo, tiempo):
        if vehiculo not in self.vehiculos:
            raise VehiculoNoEncontrado ("Vehiculo No Encontrado")
        else:
            control_tiempo = ControlDeTiempo()
            control_tiempo.validar_tiempo(tiempo)
        return vehiculo.calcular_tarifa(tiempo)

class VehiculoNoEncontrado(Exception):
    pass
class TiempoInvalido(Exception):
    pass

@dataclass
class Recibo:
    vehiculo: str
    tiempo: int
    total: float

    def __str__(self) -> str:
        return (f"Recibo:\n"
        f"Vehículo: {self.vehiculo.marca}, Placa: {self.vehiculo.placa}\n"
        f"Tiempo: {self.tiempo} horas\n"
        f"Total a pagar: ${self.total}")

@dataclass
class ControlDeTiempo():
    def validar_tiempo(self, tiempo: float):
        if not isinstance(tiempo, (int, float)):
            raise TiempoInvalido("El tiempo debe ser un número válido")
        if tiempo < 0:
            raise TiempoInvalido("El tiempo debe ser positivo")
###############################################################
try:
    auto = Automovil(placa="ABC123", marca="Toyota", tarifahora=2)
    ##
    estacionamiento = Estacionamiento()
    estacionamiento.registro_vehiculos(auto)
    ##
    tiempo = 3
    tarifa= estacionamiento.calcular_tarifa(auto, tiempo)
    print(f"Tarifa Calculada: {tarifa}")
    ##
    recibo = Recibo(vehiculo=auto, tiempo=tiempo, total=tarifa)
    print(recibo)
except TiempoInvalido as e:
    print(f"Error: {e}")
except VehiculoNoEncontrado as e:
    print(f"Error: {e}")
################################################################
