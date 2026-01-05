from net_rent import NetRent
from renta_neta import RentaNeta
import unittest

class TestRentalScripts(unittest.TestCase):
    def test_net_rent_logic(self):
        # Case 1: 10000 gross, 0.35 tax
        nr = NetRent(10000, 0.35)
        
        expected_deduction = 3500.0  # 10000 * 0.35
        expected_taxable = 6500.0    # 10000 - 3500
        expected_tax = 2275.0        # 6500 * 0.35
        expected_net = 7725.0        # 10000 - 2275
        
        self.assertAlmostEqual(nr.rent_deduction, expected_deduction)
        self.assertAlmostEqual(nr.taxable_rent, expected_taxable)
        self.assertAlmostEqual(nr.taxes_due, expected_tax)
        self.assertAlmostEqual(nr.net_rent, expected_net)
        
    def test_renta_neta_logic(self):
        # Case 1: 10000 gross, 0.35 tax (Same values but different class)
        rn = RentaNeta(10000, 0.35)
        
        expected_deduction = 3500.0
        expected_taxable = 6500.0
        expected_tax = 2275.0
        expected_net = 7725.0
        
        self.assertAlmostEqual(rn.deduccion, expected_deduction)
        self.assertAlmostEqual(rn.renta_gravable, expected_taxable)
        self.assertAlmostEqual(rn.impuestos_por_pagar, expected_tax)
        self.assertAlmostEqual(rn.renta_neta, expected_net)

if __name__ == '__main__':
    unittest.main()
