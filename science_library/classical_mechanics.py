from fundamentals_library.computations import *
from fundamentals_library.constants import *
import math

def newtonian_force(mass: float, acceleration: float):

    if mass < 0:
        
        return None
    
    return product(mass, acceleration)