import unittest
from mcgill_app.star import *
import mcgill_app.constants as constants


class StarTester(unittest.TestCase):
    """
    All data points obtained from astro.unl.edu/classaction/animations/light/bbexplorer.html.
    """

    def setUp(self):
        self.star1 = Star(constants.SOLAR_RADIUS, 10 * constants.PARSEC, 3000)
        self.star2 = Star(constants.SOLAR_RADIUS, 10 * constants.PARSEC, 4000)
        self.star3 = Star(constants.SOLAR_RADIUS, 10 * constants.PARSEC, 5000)

    def test_get_u_mag(self):
        self.assertEqual(round(self.star1.get_u_mag(), 1), 13.1)
        self.assertEqual(round(self.star2.get_u_mag(), 1), 9.3)
        self.assertEqual(round(self.star3.get_u_mag(), 1), 7.1)

    def test_get_b_mag(self):
        self.assertEqual(round(self.star1.get_b_mag(), 1), 11.0)
        self.assertEqual(round(self.star2.get_b_mag(), 1), 8.1)
        self.assertEqual(round(self.star3.get_b_mag(), 1), 6.3)

    def test_get_v_mag(self):
        self.assertEqual(round(self.star1.get_v_mag(), 1), 9.4)
        self.assertEqual(round(self.star2.get_v_mag(), 1), 7.0)
        self.assertEqual(round(self.star3.get_v_mag(), 1), 5.6)

    def test_get_r_mag(self):
        self.assertEqual(round(self.star1.get_r_mag(), 1), 8.4)
        self.assertEqual(round(self.star2.get_r_mag(), 1), 6.4)
        self.assertEqual(round(self.star3.get_r_mag(), 1), 5.2)


if __name__ == "__main__":
    unittest.main()
