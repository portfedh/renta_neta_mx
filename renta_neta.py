from dataclasses import dataclass
from typing import Optional

@dataclass
class RentaNeta:
    """
    Calcula la renta neta basada en la renta bruta y la tasa de impuestos.
    Usa una deducción ciega estándar si aplica.
    """
    renta_bruta: float
    tasa_isr: float
    DEDUCCION_CIEGA: float = 0.35

    @property
    def deduccion(self) -> float:
        return self.renta_bruta * self.DEDUCCION_CIEGA

    @property
    def renta_gravable(self) -> float:
        return self.renta_bruta - self.deduccion

    @property
    def impuestos_por_pagar(self) -> float:
        return self.renta_gravable * self.tasa_isr

    @property
    def renta_neta(self) -> float:
        return self.renta_bruta - self.impuestos_por_pagar

    @property
    def tasa_efectiva(self) -> float:
        if self.renta_bruta == 0:
            return 0.0
        return self.impuestos_por_pagar / self.renta_bruta


def get_float_input(mensaje: str, default: Optional[float] = None) -> float:
    """Función auxiliar para obtener entrada flotante con validación."""
    while True:
        entrada_usuario = input(mensaje)
        if not entrada_usuario and default is not None:
            return default
        try:
            return float(entrada_usuario)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")


def main():
    print("--- Calculadora de Renta Neta ---")
    
    renta_bruta = get_float_input("Monto de renta mensual: ")
    
    tasa_isr = get_float_input("Tasa de impuestos PF (0.0 - 0.35). Presione Enter para default (0.35): ", default=0.35)

    calculadora = RentaNeta(renta_bruta, tasa_isr)

    print("\n--- Resultados ---")
    print(f"Renta Bruta:         ${calculadora.renta_bruta:,.2f}")
    print(f"Renta neta:          ${calculadora.renta_neta:,.2f}")
    print(f"Deducción Ciega:     {calculadora.DEDUCCION_CIEGA * 100:,.2f}%")
    print(f"Deducción Ciega($):  ${calculadora.deduccion:,.2f}")
    print(f"Renta gravable:      ${calculadora.renta_gravable:,.2f}")
    print(f"Impuestos por pagar: ${calculadora.impuestos_por_pagar:,.2f}")
    print(f"Tasa efectiva:       {calculadora.tasa_efectiva * 100:,.2f}%")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")
