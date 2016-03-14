from __future__ import division
import constants
import math
import plotted_functions as pf


class Star(object):

    def __init__(self, radius, dist, surface_temp):
        """
        @type radius: float
        @param radius: Radius of star in meters.
        @type dist: float
        @param dist: Distance of star from observer in meters.
        @type surface_temp: float
        @param surface_temp: Surface temperature of star in Kelvin.
        """
        self.radius = radius
        self.dist = dist
        self.surface_temp = surface_temp

    def _get_wavelength_magnitude(self, wavelength, zero_point_flux):
        """
        Gets absolute magnitude of the star within a certain wavelength.

        @type wavelength: float
        @param wavelength: Wavelength to get magnitude of star within (m).
        @type zero_point_flux: float
        @param zero_point_flux: Flux in wavelength of reference star with zero magnitude (ie. Vega).
        @rtype: float
        @return: Magnitude of self.
        """
        flux = pf.PlottedPlanckFunction(self.surface_temp)(wavelength)
        # Get ratio of own flux to Vega's flux, ie. a reference point.
        return -2.5 * math.log(flux / zero_point_flux, 10)

    def get_u_mag(self):
        return self._get_wavelength_magnitude(constants.U_WAVELENGTH, constants.VEGA_U_FLUX)

    def get_b_mag(self):
        return self._get_wavelength_magnitude(constants.B_WAVELENGTH, constants.VEGA_B_FLUX)

    def get_v_mag(self):
        return self._get_wavelength_magnitude(constants.V_WAVELENGTH, constants.VEGA_V_FLUX)

    def get_r_mag(self):
        return self._get_wavelength_magnitude(constants.R_WAVELENGTH, constants.VEGA_R_FLUX)
