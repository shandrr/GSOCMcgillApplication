"""
.. module:: main
    :synopsis: Plot all required graphs, and prints star magnitudes in additional table.

.. moduleauthor:: Jack Romo <sharrackor@gmail.com>

"""

import graphs
import constants
import matplotlib
matplotlib.use('Agg')
import plotted_functions as pf
import star

def plot_blackbody_fluxes():
    """
    Plot graph of black body fluxes against wavelength.
    Presents curves of several black bodies, differing in their temperatures
    """
    graph = graphs.FunctionsGraph(x_label="wavelength / nm", y_label="flux / W * sr^-1 * m^-3", title="Black Body Flux")
    # Temperatures of black bodies (K) mapped to style of lines on graph.
    temps_to_styles_map = {3000.0: "g-",
                           4000.0: "b-",
                           5000.0: "r-"}
    for temp, style in temps_to_styles_map.items():
        planck_function = pf.PlottedPlanckFunction(temp)
        graph.add_plotted_function(planck_function,
                                   style=style,
                                   label=str(int(temp)) + "K")
    graph.plot(x_range=(0.1e-6, 6e-6), point_spacing=0.02e-6, unit_factor_x=10**9)


def plot_ubvr_mags():
    """
    Plots U, B, V, and R magnitudes of a star against possible temperatures between 1000K and 10_000K.
    Star has radius equal to the sun and a distance of 10 parsecs from Earth.
    """
    graph = graphs.FunctionsGraph(x_label="Temperature / K", y_label="Magnitude", title="Star UBVR Magnitudes")
    for wave_band, style in zip(["u", "b", "v", "r"], ["m-", "b-", "k-", "r-"]):
        mag_func = pf.PlottedMagnitudeFunction(constants.SOLAR_RADIUS, 10 * constants.PARSEC, wave_band)
        graph.add_plotted_function(mag_func, style=style, label=str(wave_band))
    graph.plot((1000, 10000), 10)


def print_ubvr_mags():
    """
    Prints U, B, V, and R magnitudes of a star against possible temperatures between 1000K and 10_000K.
    Star has radius equal to the sun and a distance of 10 parsecs from Earth.
    """
    print("Temperature (K)\t| U \t| B \t| V \t| R")
    print("-"*16 + ("+" + "-"*7)*4)
    for temperature in range(1000, 11000, 1000):
        st = star.Star(constants.SOLAR_RADIUS, 10*constants.PARSEC, temperature)
        print("{0}\t\t\t| {1:.1f}\t| {2:.1f}\t| {3:.1f}\t| {4:.1f}".format(temperature,
                                                                           st.get_u_mag(),
                                                                           st.get_b_mag(),
                                                                           st.get_v_mag(),
                                                                           st.get_r_mag()))


def main():
    """
    Main function of program. Called to execute entire system.
    """
    plot_blackbody_fluxes()
    plot_ubvr_mags()
    print_ubvr_mags()


if __name__ == "__main__":
    main()
