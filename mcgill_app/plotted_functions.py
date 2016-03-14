"""
.. module:: plotted_functions
    :synopsis: All PlottedFunctions, functions compatible with FunctionsGraph.

.. moduleauthor:: Jack Romo <sharrackor@gmail.com>

"""

from __future__ import division
import math
import abc
import constants
import star


class PlottedFunction(object):
    """
    Wrapper class for functions, providing methods relevant to plotting.
    Assume that functions only take one input for simplicity.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __call__(self, x):
        """
        Returns call of function. Only fitted to one variable, for simplicity's sake.

        :param x: Input value to function.
        :returns: PlottedFunction applied to x.
        """

    def list_call(self, arg_ls):
        """
        Takes a list of arguments and returns a list of corresponding results.

        :type arg_ls: list
        :param arg_ls: List of all arguments. Each will be converted into an individual result.
        :returns: List of each element of arg_ls applied to PlottedFunction.
        """
        return [self(x) for x in arg_ls]

    def get_xy_vals(self, x_range, point_spacing=1.0):
        """
        Gets two lists of points, one for x values of coordinates and one for y values.
        The two together can be used to plot the function over a given range and to a given accuracy.

        :type x_range: tuple
        :param x_range: A 2-tuple of the minimum and maximum x values to plot.
        :type point_spacing: float
        :param point_spacing: The distance between x values in range of x values used.
        :returns: Two lists, one of all x values and another of respective y values for points on graph.
        """
        x_values = [x_range[0]]
        x = x_range[0]
        while x < x_range[1]:
            x += point_spacing
            x_values.append(x)
        y_values = self.list_call(x_values)
        return x_values, y_values


class PlottedPlanckFunction(PlottedFunction):
    """
    Planck's law that relates wavelengths emitted from a black body to their amplitudes.
    """

    def __init__(self, temperature):
        """
        :type temperature: float, int
        :param temperature: Temperature of black body, in Kelvin.
        """
        self.temp = float(temperature)

    def __call__(self, l):
        """
        Calls Planck's law function on a particular wavelength of radiation.

        :type l: float, int
        :param l: Wavelength of radiation to be analyzed (m).
        :returns: Intensity of wavelength emitted by black body.
        """
        numerator = 2 * constants.PLANCK_CONST * (constants.LIGHT_SPEED ** 2)
        denominator = (l**5) * ((math.e ** ((constants.PLANCK_CONST * constants.LIGHT_SPEED) /
                                            (l * constants.BOLTZMANN_CONST * self.temp))) - 1)
        return numerator / denominator


class PlottedMagnitudeFunction(PlottedFunction):
    """
    Function to plot magnitude of star in specific wave band. Uses UBVR wavebands.
    """

    def __init__(self, radius, distance, wave_band="u"):
        """
        :type radius: int, float
        :param radius: Radius of star in meters.
        :type distance: int, float
        :param distance: Distance of star from observer in meters.
        :type wave_band: str
        :param wave_band: Wave band (u, v, b or r) to get magnitude within.
        """
        self.radius = radius
        self.distance = distance
        self.wave_band = wave_band

    def __call__(self, temperature):
        """
        Get magnitude of star in wave band if star is a specific temperature.

        :type temperature: int, float
        :param temperature: Temperature of star.
        :rtype: float
        :returns: Magnitude of star within specified wave band.
        :raises: ValueError
        """
        st = star.Star(self.radius, self.distance, temperature)
        if self.wave_band == "u":
            return st.get_u_mag()
        elif self.wave_band == "b":
            return st.get_b_mag()
        elif self.wave_band == "v":
            return st.get_v_mag()
        elif self.wave_band == "r":
            return st.get_r_mag()
        else:
            raise ValueError("Could not identify wave band")
