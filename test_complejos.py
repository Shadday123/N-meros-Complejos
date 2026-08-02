import unittest
import math
import complejos


class TestComplejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(
            complejos.suma((2, 3), (1, -4)),
            (3, -1)
        )

    def test_resta(self):
        self.assertEqual(
            complejos.resta((2, 3), (1, -4)),
            (1, 7)
        )

    def test_multiplicacion(self):
        self.assertEqual(
            complejos.multiplicacion((1, 2), (3, 4)),
            (-5, 10)
        )

    def test_division(self):
        resultado = complejos.division((0, 3), (-1, -1))
        self.assertAlmostEqual(resultado[0], -1.5)
        self.assertAlmostEqual(resultado[1], -1.5)

    def test_modulo(self):
        self.assertAlmostEqual(
            complejos.modulo((3, 4)),
            5.0
        )

    def test_conjugado(self):
        self.assertEqual(
            complejos.conjugado((3, -4)),
            (3, 4)
        )

    def test_fase(self):
        self.assertAlmostEqual(
            complejos.fase((1, 1)),
            math.pi / 4
        )

    def test_cartesiano_a_polar(self):
        polar = complejos.cartesiano_a_polar((3, 4))

        self.assertAlmostEqual(polar[0], 5)
        self.assertAlmostEqual(
            polar[1],
            math.atan2(4, 3)
        )

    def test_polar_a_cartesiano(self):
        cartesiano = complejos.polar_a_cartesiano(5, math.atan2(4, 3))

        self.assertAlmostEqual(cartesiano[0], 3)
        self.assertAlmostEqual(cartesiano[1], 4)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            complejos.division((1, 2), (0, 0))


if __name__ == "__main__":
    unittest.main()