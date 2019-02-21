import unittest
from GSOCMcgillApplication.mcgill_app.graphs import *
from mcgill_app.plotted_functions import *
import mcgill_app.constants as constants


class FunctionsGraphTester(unittest.TestCase):
    """
    Cannot test in normal fashion, as FunctionsGraph plots output graphically.
    Therefore, requires user to verify output visually.
    """

    def setUp(self):
        self.graph = FunctionsGraph(x_label="x label", y_label="y label")
        mag_func1 = PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band="u")
        mag_func2 = PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band="b")
        self.graph.add_plotted_function(mag_func1, style="g-", label="Function 1")
        self.graph.add_plotted_function(mag_func2, style="r-", label="Function 2")

    def test_plot(self):
        self.graph.plot((1000, 10000), 100)


if __name__ == "__main__":
    unittest.main()
