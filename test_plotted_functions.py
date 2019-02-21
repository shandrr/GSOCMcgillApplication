import unittest
from mcgill_app.plotted_functions import *
import mcgill_app.constants as constants


class DummyPlottedFunction1(PlottedFunction):
    """
    A dummy subclass to PlottedFunction, to be used solely for testing.
    """

    def __call__(self, x):
        return x


class DummyPlottedFunction2(PlottedFunction):
    """
    A dummy subclass to PlottedFunction, to be used solely for testing.
    """

    def __call__(self, x):
        return 0


class PlottedFunctionTester(unittest.TestCase):

    def setUp(self):
        self.func1 = DummyPlottedFunction1()
        self.func2 = DummyPlottedFunction2()

    def test_call(self):
        self.assertEqual(self.func1(1), 1)
        self.assertEqual(self.func2(1), 0)

    def test_list_call(self):
        self.assertEqual(self.func1.list_call([1, 2, 3]), [1, 2, 3])
        self.assertEqual(self.func2.list_call([1, 2, 3]), [0, 0, 0])

    def test_get_xy_vals(self):
        self.assertEqual(self.func1.get_xy_vals((0, 4), 1.0), ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]))
        self.assertEqual(self.func1.get_xy_vals((0, 2), 0.5), ([0, 0.5, 1, 1.5, 2], [0, 0.5, 1, 1.5, 2]))
        self.assertEqual(self.func2.get_xy_vals((0, 4), 0.5), ([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0],
                                                               [0 for _ in range(9)]))


class PlottedPlanckFunctionTester(unittest.TestCase):

    def setUp(self):
        self.planck1 = PlottedPlanckFunction(1000)
        self.planck2 = PlottedPlanckFunction(2000)

    def test_call(self):
        self.assertEqual(self.planck1(1), 8.278100626956567e-12)
        self.assertEqual(self.planck2(1), 1.655626089571409e-11)


class PlottedMagnitudeFunctionTester(unittest.TestCase):
    """
    Data points obtained from astro.unl.edu/classaction/animations/light/bbexplorer.html.
    """

    def setUp(self):
        self.planck_u = PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band="u")
        self.planck_b = PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band="b")
        self.planck_v = PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band="v")
        self.planck_r = PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band="r")

    def test_call(self):
        # Note: Function is not able to meet results on application exactly, accurate to 1 decimal place
        self.assertEqual(round(self.planck_u(4000), 1), 9.3)
        self.assertEqual(round(self.planck_b(4000), 1), 8.1)
        self.assertEqual(round(self.planck_v(4000), 1), 7.0)
        self.assertEqual(round(self.planck_r(4000), 1), 6.4)


if __name__ == "__main__":
    unittest.main()
