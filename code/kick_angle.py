from scipy.constants import physical_constants as const
import numpy as np

p = 5.392 # GeV/c, proton momentum for the cycle
Brho = p*3.3356 # Tm, magnetic rigidity

def kick_angle(voltage):
    """
    Calculates the angular kick to a proton beam of rigidity `Brho` [Tm] from a pair of TFB electrodes with voltage `voltage` [V].
    """

    c = const["speed of light in vacuum"][0] # [m/s] speed of light
    E0 = const["proton mass energy equivalent in MeV"][0]*1e6 # eV
    mu0 = const["vacuum mag. permeability"][0] # H/m, vacuum permeability

    T = (np.sqrt(p**2+E0/1e9**2)-E0/1e9)*1e9 # eV, proton KE
    P = 5e3 # W, TFB peak power / electrode
    Z = 100 # Ohm, TFB impedance / electrode

    L = 935e-3 # m, TFB length
    r = 70e-3 # m, TFB separation

    E = T + E0 # Total Energy
    gamma = E / E0 # Normalized energy (lorentz)
    beta = np.sqrt(1-gamma**-2) # normalised velocity (lorentz)
    cp = p*1e9 # eV, particle momentum

    # Electric Field
    Vp = np.sqrt(P * Z * 2) # peak voltage
    V = Vp * voltage
    Efield = V / r # adjusted for gain

    # Magnetic Field
    I = np.sqrt((V**2/Z)/Z*2) # current
    Hfield = (2*I) / (2*np.pi*r) # adjusted for gain
    Bfield = Hfield * mu0

    # Angle
    theta_M = c/1e9*Bfield*L / (cp/10**9)
    theta_E = Efield/1e9*L / (cp/10**9 * beta)
    theta = theta_E + theta_M
    return theta