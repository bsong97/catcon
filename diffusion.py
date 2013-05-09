import math


class diffusion:
    """To calculate bulk diffusion coefficient, based on Stefan-Maxwell hard sphere model"""
    def __init__(self, M1, M2, V1, V2):
        self.M1 = M1
        self.M2 = M2
        self.V1 = V1
        self.V2 = V2
    
    def bulk(self):
        return (1.013e-2*Tk(i)**1.75*((1/Mco)+(1/Mair))^(1/2))/(P*(Vco^(1/3)+Vair^(1/3))^2)
    
    def diserpsion(self):
        pass
    
    