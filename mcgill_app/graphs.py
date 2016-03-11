from __future__ import division
import constants
import math
import abc
import matplotlib.pyplot as plt


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
        if not (isinstance(l, float) or isinstance(l, int)):
            raise TypeError("Must provide numerical input to PlottedPlanckFunction")

        numerator = 2 * constants.PLANCK_CONST * (constants.LIGHT_SPEED ** 2)
        denominator = (l**5) * ((math.e ** ((constants.PLANCK_CONST * constants.LIGHT_SPEED) /
                                            (l * constants.BOLTZMANN_CONST * self.temp))) - 1)
        return numerator / denominator
