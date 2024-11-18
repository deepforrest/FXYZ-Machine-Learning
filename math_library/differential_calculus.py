from fundamentals_library.computations import *
from fundamentals_library.constants import *
import math

def polynomial_point_derivative(coeff: float, base: float, power: float) -> float:

    # Checks for instances of divide by 0 and/or indeterminant forms
    if power <= ZEROTH_POWER and base == ZERO_BASE:
        
        return None

    return polynomial(product(coeff, power), base, subtract_one(power))

def log_point_derivative(point: float, base: float, vertical_stretch: float, horizontal_stretch: float, horizontal_displacement: float, vertical_displacement: float) -> float

    # Domain needs to be tested:

    numerator: float = product(vertical_stretch, horizontal_stretch)
    denominator: float = product(math.log(base, math.e), difference(product(horizontal_stretch, point), horizontal_stretch))

    return float_quotient(numerator, denominator)


def exp_point_derivative(point: float, base: float, vertical_stretch: float, horizontal_stretch: float, horizontal_displacement: float, vertical_displacement: float) -> float:


    original_function: float = product(vertical_stretch, exponentiate(base, difference(product(horizontal_stretch, point), horizontal_displacement)))
    exp_derivative: float =  product(horizontal_displacement, math.log(base, math.e))

    return product(original_function, exp_derivative)

# Unfinished
def find_critical_points(poly_coeff_arr: list) -> list:

    poly_der_coeffs = []
    highest_power = len(poly_coeff_arr) - 1
    # Generate a new arr of coefficients

    return -1

