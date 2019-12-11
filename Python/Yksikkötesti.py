import unittest

class OmaJuttu:
    """Yksinkertainen testiluokka."""
    def oma_metodi(self):
        """Oma testimetodini."""
        print("Moi!")
        return 5+5

class TestSum(unittest.TestCase):
    """Yksikkötestiluokka."""

    def test_sum(self):
        """Testaa taulukon summan laskennan."""
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        """Testaa tuple-tyypin summan laskennan."""

        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

    def testaa_olio(self):
        """Testaa olion metodin kutsun."""
        om = OmaJuttu()
        tulos = om.oma_metodi()
        self.assertEqual(tulos, 10, "Tuloksen pitäisi olla 10.")

if __name__ == '__main__':
    om = OmaJuttu()
    om.oma_metodi()
    unittest.main()
