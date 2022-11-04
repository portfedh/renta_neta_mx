
class NetRent():

    TAX_ABATEMENT = 0.35

    def __init__(self):
        self.get_inputs()
        self.calculate_net_rent()
        self.print_output()

    def get_inputs(self):
        self.gross_rent = float(input("Input monthly gross rent: "))
        self.tax_rate = float(input("Input your tax rate (0.0 - 0.35). Use 0.35 if you dont know: "))

    def calculate_net_rent(self):
        self.rent_deduction = self.gross_rent * NetRent.TAX_ABATEMENT
        self.taxable_rent = self.gross_rent - self.rent_deduction
        self.taxes_due = self.taxable_rent * self.tax_rate
        self.net_rent = self.gross_rent - self.taxes_due
        self.effective_tax_rate = self.taxes_due / self.gross_rent

    def print_output(self):
        print("Gross rent: " + "$" + "{:,.2f}".format(self.gross_rent))
        print("Net rent: " + "$" + "{:,.2f}".format(self.net_rent))
        print("Tax Abatement: " + "{:,.2f}".format(NetRent.TAX_ABATEMENT*100) + "%")
        print("Rent Deduction: " + "$" + "{:,.2f}".format(self.rent_deduction))
        print("Taxable rent: " + "$" + "{:,.2f}".format(self.taxable_rent))
        print("Taxes due: " + "$"  + "{:,.2f}".format(self.taxes_due))
        print("Effective tax rate: " + "{:,.2f}".format(self.effective_tax_rate*100) + "%")


if __name__ == "__main__":
    oNetRent = NetRent()
