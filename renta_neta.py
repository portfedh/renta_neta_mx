# Constantes
deduccion_ciega = 0.35
tasa_isr_pf = 0.35 # Tasa Mamxima

# Obtener la renta del usuario
renta_bruta = float(input("¿Cuál es la renta mensual?: "))
tasa_isr_input = float(input("¿Cuál es la tasa de ISR? (Si no se conoce usar 0.35): "))

# Calculos
deduccion = renta_bruta * deduccion_ciega
renta_gravable = renta_bruta - deduccion
impuestos_por_pagar = renta_gravable * tasa_isr_input
tasa_efectiva = impuestos_por_pagar/renta_bruta
renta_neta = renta_bruta - impuestos_por_pagar


# Outputs
if __name__ == "__main__":
    print("Renta Bruta: " + "$" + "{:,.2f}".format(renta_bruta))
    print("Renta neta: " + "$" + "{:,.2f}".format(renta_neta))
    print("Deduccion Ciega: " + "{:,.2f}".format(deduccion_ciega*100) + "%")
    print("Deduccion Ciega: " + "$" + "{:,.2f}".format(deduccion))
    print("Renta Gravable: " + "$" + "{:,.2f}".format(renta_gravable))
    print("Impuestos por pagar: " + "$"  + "{:,.2f}".format(impuestos_por_pagar))
    print("Tasa efectiva: " + "{:,.2f}".format(tasa_efectiva*100) + "%")

