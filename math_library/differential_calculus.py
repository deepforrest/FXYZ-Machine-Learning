from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *
import math


def poly_term_pt_der(coeff: float, base: float, power: float) -> float:

    # Checks for instances of divide by 0 and/or indeterminant forms
    if power <= ZEROTH_POWER and base == ZERO_BASE:
        
        return None

    new_coeff = product(coeff, power)
    new_power = subtract_one(power)

    return polynomial(new_coeff, base, new_power)


def log_gen_pt_der(point: float, base: float, vertical_stretch: float, horizontal_stretch: float, horizontal_displacement: float, vertical_displacement: float) -> float:

    # Domain needs to be tested:

    numerator: float = product(vertical_stretch, horizontal_stretch)
    denominator: float = product(math.log(base, math.e), difference(product(horizontal_stretch, point), horizontal_stretch))

    return float_quotient(numerator, denominator)


def exp_gen_pt_der(point: float, base: float, vertical_stretch: float, horizontal_stretch: float, horizontal_displacement: float, vertical_displacement: float) -> float:

    original_function: float = product(vertical_stretch, exponentiate(base, difference(product(horizontal_stretch, point), horizontal_displacement)))
    exp_derivative: float =  product(horizontal_displacement, math.log(base, math.e))

    return product(original_function, exp_derivative)

# Fix 
def exp_poly_pt_der(point: float, base: float, poly_coeff_arr: list[float]) -> float:

    der_poly_arr: list[float] = []
    poly_power = get_highest_power(poly_coeff_arr)

    power = poly_power

    for coeff in poly_coeff_arr:

        der_poly_arr.append(product(power, poly_coeff_arr[coeff]))
        power -= 1

    poly_der_value = SUM_INIT
    der_power = subtract_one(poly_power)

    for coeff in der_poly_arr:

        poly_der_value += poly_pt_der_arr(der_poly_arr[coeff], point, der_power)
        der_power -= 1

    der_value: float = product(poly_der_value, math.log(base, math.e))

    # Needs changed to actual formula
    exp_value = 1

    return product(der_value, exponentiate(point, exp_value))
    
    
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
def find_critical_points(poly_coeff_arr: list[float]) -> list[float]:

    poly_der_coeffs = []
    power = get_highest_power(poly_coeff_arr)
    # Generate a new arr of coefficients

    return -1

def slope_of_circle_at_pt(point_arr: list[float], vertex: list[float] = [0, 0]) -> float:

    if not validate_point(point_arr, POINT_LEN_2D) or not validate_point(vertex, POINT_LEN_2D):

        return None

    numerator = neg(difference(point_arr[X_IND], vertex[X_IND]))
    denominator = difference(point_arr[Y_IND], vertex[Y_IND])

    return float_quotient(numerator, denominator) if denominator != ZERO_DENOM else f'Undefined slope!'