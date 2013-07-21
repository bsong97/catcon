import math
import gas
from gas import CO, propane, air, O2, CO2

class diffusion:
    """To calculate bulk diffusion coefficient, based on Stefan-Maxwell hard sphere model"""
    def __init__(self, gas1, gas2):
        self.M1 = gas1.mm
        self.M2 = gas2.mm
        self.V1 = gas1.mv
        self.V2 = gas2.mv
    
    def bulk(self, T, P):
        return (1.013e-2*T**1.75*((1/self.M1)+(1/self.M2))**(1/2))/(P*(self.V1**(1/3)+self.V2**(1/3))**2)
    
    def dispersion(self, v):
        """Based on Taylor-Aris dispersion model"""
        vel = self.v
        return self.bulk + vel
    
class advection:
    pass

class mass_transfer:
    """Based on Sherwood number"""
    
    pass

class pore_diffusion:
    pass

class reaction:
    """Combustion reaction"""
    def CO():
        pass
    
    def HC():
        pass



# test
#def _test():
    #a = diffusion(CO(), air())
    #coeff = a.bulk(273, 1.01e5)
    #print coeff
#
#
#_test()