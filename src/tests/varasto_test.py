import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.negVarasto = Varasto(-1, -1)
        self.pieniVarasto = Varasto(1, 2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_on_nolla(self):
        self.assertAlmostEqual(self.negVarasto.tilavuus, 0)

    def test_negatiivinen_saldo_on_nolla(self):
        self.assertAlmostEqual(self.negVarasto.saldo, 0)

    def test_saldo_ei_mahdu(self):
        self.assertAlmostEqual(self.pieniVarasto.saldo, 1)

    def test_lisaa_negatiivinen(self):
        alku_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(alku_saldo, self.varasto.saldo)
    
    def test_lisaa_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(10000)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ota_negatiivinen(self):
        alku_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(alku_saldo, self.varasto.saldo)
    
    def test_ota_enemman_kuin_varastossa(self):
        self.varasto.ota_varastosta(10000)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_str_on_oikein(self):
        self.assertAlmostEqual(str(Varasto(10, 4)), "saldo = 5, vielä tilaa 6")