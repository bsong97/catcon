# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:33:55 2013

@author: bsong97
"""

import gas

# Exhaust gas with various concentration of elemental gas
class exhaust:
    def __init__(self, vel, T, P, CO, HC, NOx, CO2, O2=None):
        """The exhaust gas"""
        self.vel = vel          # linear mean fluid velocity, m/s
        self.temp = T           # temperature, K
        self.pres = P           # pressure, Pa
        self.CO = CO            # CO concentration, ppm
        self.HC = HC            # HC concentration (represented by propane), ppm
        self.NOx = NOx          # NOx concentration, ppm
        self.CO2 = CO2          # CO2 concentration, ppm
        self.O2 = O2            # O2 concentration, ppm
        

# Data from experiment
vmean = 2.4     # linear mean fluid velocity
T_in = 417      # inlet temperature
P_in = 101325   # inlet pressure
CO_in = 3e3/1e6 # inlet CO concentration
HC_in = 500/1e6 # inlet propane concentration
NOx_in = 0      # inlet NOx concentration
CO2_in = 0      # inlet CO2 concentration

# Specifying inlet and initial condition for the exhaust gas
inlet = exhaust(vmean, T_in, P_in, CO_in, HC_in, NOx_in, CO2_in)
initial = inlet


