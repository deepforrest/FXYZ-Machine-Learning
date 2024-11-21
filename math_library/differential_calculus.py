from fundamentals_library.computations import *
from fundamentals_library.constants import *
import math


def poly_term_pt_der(coeff: float, base: float, power: float) -> float:

    # Checks for instances of divide by 0 and/or indeterminant forms
    if power <= ZEROTH_POWER and base == ZERO_BASE:
        
        return None

    return polynomial(product(coeff, power), base, subtract_one(power))


def log_pt_der(point: float, base: float, vertical_stretch: float, horizontal_stretch: float, horizontal_displacement: float, vertical_displacement: float) -> float:

    # Domain needs to be tested:

    numerator: float = product(vertical_stretch, horizontal_stretch)
    denominator: float = product(math.log(base, math.e), difference(product(horizontal_stretch, point), horizontal_stretch))

    return float_quotient(numerator, denominator)


def exp_pt_der(point: float, base: float, vertical_stretch: float, horizontal_stretch: float, horizontal_displacement: float, vertical_displacement: float) -> float:

    original_function: float = product(vertical_stretch, exponentiate(base, difference(product(horizontal_stretch, point), horizontal_displacement)))
    exp_derivative: float =  product(horizontal_displacement, math.log(base, math.e))

    return product(original_function, exp_derivative)

# Unfinished
def poly_pt_der_arr(coeff_arr: list, point: int) -> float:

    # A number in this function is an assumed constant, and d/dx of c = 0
    if len(coeff_arr) < 2: return 0

    power = get_highest_power(coeff_arr)
    point_value = SUM_INIT

    for coeff in coeff_arr:

        point_value += poly_term_pt_der(coeff_arr[coeff], point, power)
        power -= 1

    return point_value


# Unfinished
def find_critical_points(poly_coeff_arr: list) -> list:

    poly_der_coeffs = []
    highest_power = subtract_one(len(poly_coeff_arr))
    # Generate a new arr of coefficients

    return -1