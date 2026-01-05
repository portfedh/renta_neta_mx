from dataclasses import dataclass
from typing import Optional

@dataclass
class NetRent:
    """
    Calculates net rent based on gross rent and tax rate.
    Uses a standard tax abatement (blind deduction) if applicable.
    """
    gross_rent: float
    tax_rate: float
    TAX_ABATEMENT: float = 0.35

    @property
    def rent_deduction(self) -> float:
        return self.gross_rent * self.TAX_ABATEMENT

    @property
    def taxable_rent(self) -> float:
        return self.gross_rent - self.rent_deduction

    @property
    def taxes_due(self) -> float:
        return self.taxable_rent * self.tax_rate

    @property
    def net_rent(self) -> float:
        return self.gross_rent - self.taxes_due

    @property
    def effective_tax_rate(self) -> float:
        if self.gross_rent == 0:
            return 0.0
        return self.taxes_due / self.gross_rent


def get_float_input(prompt: str, default: Optional[float] = None) -> float:
    """
    Asks the user for a number and validates the input.
    
    Parameters:
    - mensaje: The prompt to show the user
    - default: Optional default value if user just presses Enter
    
    Returns:
    - A valid float number
    """
    while True:
        user_input = input(prompt)
        if not user_input and default is not None:
            return default
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("--- Net Rent Calculator ---")
    
    gross_rent = get_float_input("Input monthly gross rent: ")
    
    # Prompt implies a default of 0.35 if unknown, though original code asked user to input it.
    # We'll allow the user to just press enter for 0.35 if they don't know (0.35 is strictly max rate, but following logic).
    # Wait, original said: "Use 0.35 if you dont know".
    tax_rate = get_float_input("Input your tax rate (0.0 - 0.35). Press Enter for default (0.35): ", default=0.35)

    calculator = NetRent(gross_rent, tax_rate)

    print("\n--- Results ---")
    print(f"Gross rent:         ${calculator.gross_rent:,.2f}")
    print(f"Net rent:           ${calculator.net_rent:,.2f}")
    print(f"Tax Abatement:      {calculator.TAX_ABATEMENT * 100:,.2f}%")
    print(f"Rent Deduction:     ${calculator.rent_deduction:,.2f}")
    print(f"Taxable rent:       ${calculator.taxable_rent:,.2f}")
    print(f"Taxes due:          ${calculator.taxes_due:,.2f}")
    print(f"Effective tax rate: {calculator.effective_tax_rate * 100:,.2f}%")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
