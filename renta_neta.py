
class RentaNeta():

    DEDUCCION_CIEGA = 0.35

    def __init__(self):
        self.get_inputs()
        self.calculate_net_rent()
        self.print_output()

    def get_inputs(self):
        self.renta_bruta = float(input("Monto de renta mensual: "))
        self.tasa_isr = float(input("Tasa de impuestos PF: (0.0 - 0.35). Usar 0.35 si no la conoces. "))

    def calculate_net_rent(self):
        self.deduccion = self.renta_bruta * RentaNeta.DEDUCCION_CIEGA
        self.renta_gravable = self.renta_bruta - self.deduccion
        self.impuestos_por_pagar = self.renta_gravable * self.tasa_isr
        self.renta_neta = self.renta_bruta - self.impuestos_por_pagar
        self.tasa_efectiva = self.impuestos_por_pagar / self.renta_bruta

    def print_output(self):
        print("Renta Bruta: " + "$" + "{:,.2f}".format(self.renta_bruta))
        print("Renta neta: " + "$" + "{:,.2f}".format(self.renta_neta))
        print("Deduccion Ciega: " + "{:,.2f}".format(RentaNeta.DEDUCCION_CIEGA*100) + "%")
        print("Deduccion Ciega: " + "$" + "{:,.2f}".format(self.deduccion))
        print("Renta gravable: " + "$" + "{:,.2f}".format(self.renta_gravable))
        print("Impuestos por pagar: " + "$"  + "{:,.2f}".format(self.impuestos_por_pagar))
        print("Tasa efectiva: " + "{:,.2f}".format(self.tasa_efectiva*100) + "%")


if __name__ == "__main__":
    oNetRent = RentaNeta()
