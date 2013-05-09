# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:33:55 2013

@author: bsong97
"""

# Properties of gas
class gas:
    def __init__(self, mm):
        self.mm = mm            # molar mass, g/mol
        



# Exhaust gas with various concentration of elemental gas
class exhaust:
    def __init__(self, vel, T, P, CO, O2, HC, NOx):
        """The exhaust gas"""
        self.vel = vel          # velocity
        self.temp = T           # temperature
        self.pres = P           # pressure
        self.CO = CO            # CO concentration
        self.O2 = O2            # Oxygen concentration
        self.HC = HC            # HC concentration (represented by propane)
        self.NOx = NOx          # NOx concentration
        

class inlet(exhaust):
    """Inlet condition"""
    pass

class initial(exhaust):
    """Initial condition"""
    pass
