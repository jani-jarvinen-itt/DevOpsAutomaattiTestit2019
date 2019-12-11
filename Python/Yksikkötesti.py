import unittest

class OmaJuttu:
    def oma_metodi(self):
        print("Moi!")
        return 5+5

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

    def testaa_olio(self):
        om = OmaJuttu()
        tulos = om.oma_metodi()
        self.assertEqual(tulos, 10, "Tuloksen pitäisi olla 10.")


if __name__ == '__main__':
    om = OmaJuttu()
    om.oma_metodi()
    unittest.main()
