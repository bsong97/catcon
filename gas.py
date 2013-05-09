# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:17:03 2013

@author: bsong97
"""

# Properties of gas
class gas:
    def __init__(self, name, mm, mv):
        self.name = name
        self.mm = mm            # molar mass, kg/kmol
        self.mv = mv            # molecular volume in m3/kmol in liquid form at its b.p.
        
    #def __str__(self):
        #return "%s has molar mass of %s g/mol and molecular volume of %s m3/kmol" % (self.name, self.mm, self.mv)


class CO(gas):
    def __init__(self):
        gas.__init__(self, 'CO', 28.01, 18.9)

class O2(gas):
    def __init__(self):
        gas.__init__(self, 'O2', 32.00, 0.00)
        
class air(gas):
    def __init__(self):
        gas.__init__(self, 'air', 28.96, 20.1)

class propane(gas):
    def __init__(self):
        gas.__init__(self, 'C3H8', 44.10, 65.34)
        
class CO2(gas):
    def __init__(self):
        gas.__init__(self, 'CO2', 44.01, 22.26)
        
        
# Testing
#def _test():
    #co = CO()
    #hc = propane()
    #print co.mm
    #print hc.mm
    #
#_test()

#CO.mm