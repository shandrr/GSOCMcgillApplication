"""
.. module:: graphs
    :synopsis: All graph plotting and creation facilities.

.. moduleauthor:: Jack Romo <sharrackor@gmail.com>

"""

from __future__ import division
import matplotlib.pyplot as plt


class FunctionsGraph(object):
    """
    A graph that wraps around matplotlib.pyplot for plotting PlottableFunctions.
    """

    def __init__(self, x_label="", y_label="", title=""):
        """
        :type x_label: str
        :param x_label: Label of x axis.
        :type y_label: str
        :param y_label: Label of y axis.
        :type title: str
        :param title: Title of graph displayed directly above.
        """
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.functions = []

    def add_plotted_function(self, func, style="g-", label=""):
        """
        Append a PlottedFunction to the graph, which will be drawn on the graph when plotted.

        :type func: PlottedFunction
        :param func: The function to be added to the graph.
        :type style: str
        :param style: The styling of the function's line on the graph. Must be in matplotlib style.
        :type label: str
        :param label: Name of function that will be put in legend of graph.
        :returns: Nothing.
        """
        self.functions.append({"function": func,
                               "style": style,
                               "label": label})

    def plot(self, x_range=(0, 10), point_spacing=1.0, unit_factor_x=1.0, unit_factor_y=1.0):
        """
        Plots graph of all functions across a specified interval.

        :type x_range: tuple
        :param x_range: A 2-tuple specifying lowest and highest x values on x-axis.
        :type point_spacing: float
        :param point_spacing: The space between x values of each plotted point on the graph.
        :type unit_factor_x: float
        :param unit_factor_x: Factor to multiply x values by to get into correct units on graph.
        :type unit_factor_y: float
        :param unit_factor_y: Factor to multiply x values by to get into correct units on graph.
        :returns: Nothing.
        """
        for func_map in self.functions:
            function = func_map["function"]
            xs, ys = function.get_xy_vals(x_range=x_range, point_spacing=point_spacing)
            plt.plot([x * unit_factor_x for x in xs],
                     [y * unit_factor_y for y in ys], func_map["style"], label=func_map["label"])
        plt.legend()
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.suptitle(self.title, fontsize=12)
        plt.show()
