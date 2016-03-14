import graphs
import star
import constants


def plot_blackbody_fluxes():
    """
    Plot graph of black body fluxes against wavelength.
    Presents curves of several black bodies, differing in their temperatures
    """
    graph = graphs.FunctionsGraph(x_label="wavelength / m", y_label="flux / W * sr^-1 * m^-3")
    # Temperatures of black bodies (K) mapped to style of lines on graph.
    temps_to_styles_map = {3000.0: "g-",
                           4000.0: "b-",
                           5000.0: "r-"}
    for temp, style in temps_to_styles_map.items():
        planck_function = graphs.PlottedPlanckFunction(temp)
        graph.add_plotted_function(planck_function,
                                   style=style,
                                   label=str(int(temp)) + "K")
    graph.plot(x_range=(0.1e-6, 6e-6), point_spacing=0.02e-6)


def display_ubvr_mags():
    """
    Displays U, B, V, and R magnitudes of a star with radius equal to the sun and a distance of 10 parsecs from Earth.
    Shows table for stars with temperatures from 1000K to 10000K.
    """
    # TODO: replace this with a graph
    print("Temperature (K)\t| U \t| B \t| V \t| R")
    print("-"*16 + ("+" + "-"*7)*4)
    for temperature in range(1000, 11000, 1000):
        st = star.Star(constants.SOLAR_RADIUS, 10*constants.PARSEC, temperature)
        u_mag, b_mag, v_mag, r_mag = st.get_ubvr_magnitudes()
        print("{0}\t\t\t| {1:.2f}\t| {2:.2f}\t| {3:.2f}\t| {4:.2f}".format(temperature, u_mag, b_mag, v_mag, r_mag))


def main():
    plot_blackbody_fluxes()
    display_ubvr_mags()


if __name__ == "__main__":
    main()
