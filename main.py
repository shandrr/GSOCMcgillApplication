from __future__ import division
from matplotlib import pyplot as plt
import abc
import math


class FunctionsGraph(object):
    """
    A graph that wraps around matplotlib.pyplot for plotting PlottableFunctions.
    """

    def __init__(self, x_label="", y_label=""):
        """
        @type x_label: str
        @param x_label: Label of x axis.
        @type y_label: str
        @param y_label: Label of y axis.
        """
        self.x_label = x_label
        self.y_label = y_label
        self.functions = []

    def add_plotted_function(self, func, style="g-", label=""):
        """
        Append a PlottedFunction to the graph, which will be drawn on the graph when plotted.

        @type func: PlottedFunction
        @param func: The function to be added to the graph.
        @type style: str
        @param style: The styling of the function's line on the graph. Must be in matplotlib style.
        @type label: str
        @param label: Name of function that will be put in legend of graph.
        @return: Nothing.
        """
        if not isinstance(func, PlottedFunction):
            raise TypeError("Must provide PlottedFunction to FunctionsGraph")
        self.functions.append({"function": func,
                               "style": style,
                               "label": label})

    def plot(self, x_range=(0, 10), point_spacing=1.0):
        """
        Plots graph of all functions across a specified interval.

        @type x_range: tuple
        @param x_range: A 2-tuple specifying lowest and highest x values on x-axis.
        @type point_spacing: float
        @param point_spacing: The space between x values of each plotted point on the graph.
        """
        for func_map in self.functions:
            function = func_map["function"]
            xs, ys = function.get_xy_vals(x_range=x_range, point_spacing=point_spacing)
            plt.plot(xs, ys, func_map["style"], label=func_map["label"])
        plt.legend()
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()


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

        @param x: Input value to function.
        @return: PlottedFunction applied to x.
        """

    def list_call(self, arg_ls):
        """
        Takes a list of arguments and returns a list of corresponding results.

        @type arg_ls: list
        @param arg_ls: List of all arguments. Each will be converted into an individual result.
        @return: List of each element of arg_ls applied to PlottedFunction.
        """
        return [self(x) for x in arg_ls]

    def get_xy_vals(self, x_range, point_spacing=1.0):
        """
        Gets two lists of points, one for x values of coordinates and one for y values.
        The two together can be used to plot the function over a given range and to a given accuracy.

        @type x_range: tuple
        @param x_range: A 2-tuple of the minimum and maximum x values to plot.
        @type point_spacing: float
        @param point_spacing: The distance between x values in range of x values used.
        @return: Two lists, one of all x values and another of respective y values for points on graph.
        """
        if not len(x_range) == 2:
            raise ValueError("Range of x values can only contain two values")
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
        @type temperature: float, int
        @param temperature: Temperature of black body, in Kelvin.
        """
        if not (isinstance(temperature, float) or isinstance(temperature, int)):
            raise TypeError("Must provide a number for temperature")
        self.temp = temperature

    def __call__(self, l):
        """
        Calls Planck's law function on a particular wavelength of radiation.

        @type l: float, int
        @param l: Wavelength of radiation to be analyzed (m).
        @return: Intensity of wavelength emitted by black body.
        """
        # QUESTION: I'm not sure exactly what number of decimal places constants should be to.
        if not (isinstance(l, float) or isinstance(l, int)):
            raise TypeError("Must provide numerical input to PlottedPlanckFunction")
        boltzmann_const = 1.38064852e-23   # J / K
        planck_const = 6.63607004e-34      # J * s
        light_speed = 299792458            # m / s

        numerator = 2 * planck_const * (light_speed**2)
        denominator = (l**5) * ((math.e**((planck_const * light_speed) / (l * boltzmann_const * self.temp))) - 1)
        return numerator / denominator


class Star(object):

    def __init__(self, radius, dist, surface_temp):
        """
        @type radius: float
        @param radius: Radius of star in meters.
        @type dist: float
        @param dist: Distance of star from observer in parsecs.
        @type surface_temp: float
        @param surface_temp: Surface temperature of star in Kelvin.
        """
        self.radius = radius
        self.dist = dist
        self.surface_temp = surface_temp

    def get_luminosity(self):
        """
        Gets overall luminosity of star based on temperature and surface area. Assume star is black body.

        @return: Luminosity of star.
        """
        stefan_boltzmann_const = 5.67e-8    # J
        area = 4 * math.pi * (self.radius**2)
        return stefan_boltzmann_const * area * (self.surface_temp**4)

    def _get_wavelength_magnitude(self, wavelength, zero_mag_flux=1.0):
        """
        Gets absolute magnitude of the star within a certain wavelength.
        Assumes that both self and Vega are black bodies.

        @type wavelength: float
        @param wavelength: Wavelength to get magnitude of star within (m).
        @type zero_mag_flux: float
        @param zero_mag_flux: Flux emitted of wavelength by a reference star with zero magnitude (Vega).
        """
        # TODO: get data about vega
        vega_surface_temp = 9602
        vega_surface_area = 1
        vega_distance = 1
        power_per_sq_meter = PlottedPlanckFunction(self.surface_temp)(wavelength)
        surface_area = 4 * math.pi * (self.radius**2)
        luminosity = power_per_sq_meter * surface_area
        power_per_sq_meter = PlottedPlanckFunction(vega_surface_temp)(wavelength)
        vega_luminosity = power_per_sq_meter * vega_surface_area
        flux = zero_mag_flux * (luminosity / vega_luminosity) * ((self.dist / vega_distance)**2)
        magnitude = -2.5 * math.log(flux / zero_mag_flux, 10)
        return magnitude

    def get_ubvr_magnitudes(self):
        """
        Gets magnitude of star in U, B, V, and R wavelengths.

        @return: 4-tuple of U, B, V and R magnitudes in order.
        """
        # TODO: get data for wavelengths and zero magnitude fluxes
        u_mag = self._get_wavelength_magnitude(1, zero_mag_flux=1)
        b_mag = self._get_wavelength_magnitude(1, zero_mag_flux=1)
        v_mag = self._get_wavelength_magnitude(1, zero_mag_flux=1)
        r_mag = self._get_wavelength_magnitude(1, zero_mag_flux=1)
        return u_mag, b_mag, v_mag, r_mag


def main():
    """
    Plots graph of black body emission wavelengths against amplitudes, then UBVR magnitudes of a star.
    """
    graph = FunctionsGraph(x_label="wavelength / m", y_label="amplitude")
    # Temperatures of black bodies (K) mapped to style of lines on graph.
    temps_to_styles_map = {3000.0: "g-",
                           4000.0: "b-",
                           5000.0: "r-"}
    for temp, style in temps_to_styles_map.items():
        planck_function = PlottedPlanckFunction(temp)
        graph.add_plotted_function(planck_function,
                                   style=style,
                                   label=str(int(temp)) + "K")
    graph.plot(x_range=(0.1e-6, 6e-6), point_spacing=0.02e-6)
    # TODO: input required parameters
    star = Star(1, 10, 4000)
    print star.get_ubvr_magnitudes()


if __name__ == "__main__":
    main()
