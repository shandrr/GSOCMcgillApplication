from __future__ import division
import graphs
import constants
import math


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
        power_per_sq_meter = graphs.PlottedPlanckFunction(self.surface_temp)(wavelength)
        surface_area = 4 * math.pi * (self.radius**2)
        luminosity = power_per_sq_meter * surface_area
        vega_power_per_sq_meter = graphs.PlottedPlanckFunction(constants.VEGA_SURFACE_TEMP)(wavelength)
        vega_luminosity = vega_power_per_sq_meter * constants.VEGA_SURFACE_AREA
        flux = zero_mag_flux * (luminosity / vega_luminosity) * ((self.dist / constants.VEGA_DISTANCE) ** 2)
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
