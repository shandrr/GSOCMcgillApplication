import graphs
import star
import constants


def main():
    """
    Plots graph of black body emission wavelengths against amplitudes, then UBVR magnitudes of a star.
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
    st = star.Star(constants.SOLAR_RADIUS, 10*constants.PARSEC, 6000)
    print st.get_ubvr_magnitudes()


if __name__ == "__main__":
    main()
