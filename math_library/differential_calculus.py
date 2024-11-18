from fundamentals_library.computations import *
from fundamentals_library.constants import *

def polynomial_derivative(coeff: float, base: float, power: float) -> float:

    # Checks for instances of divide by 0 and/or indeterminant forms
    if power <= ZEROTH_POWER and base == ZERO_BASE:
        
        return None

    return polynomial(product(coeff, power), base, subtract_one(power))