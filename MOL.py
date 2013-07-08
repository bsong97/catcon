# Method of Lines method 
# to discretize all but one dimension
# effectively turning PDEs into ODEs
# and therefore ODESolver can be used to solve

# Requirement:
# PDE should be an Initial Value Problem (Cauchy problem) because ODE integrators are IVP
# Thus, elliptic equations such as Laplace equation cannot be used

import numpy as np

class MOL:
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = f
    
    def convert(f):
        """Take in the PDE and convert to ODE"""
        # Discretize 

