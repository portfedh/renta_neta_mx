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


def format_currency(value: float) -> str:
    """Devuelve un monto con formato monetario legible."""
    return f"${value:,.2f}"


def format_percentage(value: float) -> str:
    return f"{value * 100:,.2f}%"


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

    resultados = [
        ("Renta Bruta", format_currency(calculadora.renta_bruta)),
        ("Deducción Ciega", format_percentage(calculadora.DEDUCCION_CIEGA)),
        ("Deducción Ciega ($)", format_currency(calculadora.deduccion)),
        ("Renta Gravable", format_currency(calculadora.renta_gravable)),
        ("Tasa ISR", format_percentage(calculadora.tasa_isr)),
        ("Impuestos por pagar", format_currency(calculadora.impuestos_por_pagar)),
        ("Renta Neta", format_currency(calculadora.renta_neta)),
        ("Tasa Efectiva", format_percentage(calculadora.tasa_efectiva)),
    ]

    label_width = max(len(label) for label, _ in resultados) + 2
    value_width = max(len(value) for _, value in resultados)
    total_width = label_width + value_width

    print("\n--- Resultados ---")
    print("-" * total_width)
    for label, value in resultados:
        print(f"{label:<{label_width}}{value:>{value_width}}")
    print("-" * total_width)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")
