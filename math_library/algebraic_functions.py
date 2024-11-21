from fundamentals_library.computations import *
from fundamentals_library.constants import *
from math_library.number_theory import *
from math_library.differential_calculus import *
import math

def reduce_fraction(num: int, denom: int) -> list:
    # Get unique factors of numerator and denominator
    num_factors = factors(num)
    denom_factors = factors(denom)

    # Remove common factors
    for factor in num_factors[:]:
        
        if factor in denom_factors:
        
            num_factors.remove(factor)
            denom_factors.remove(factor)

    # Calculate the reduced numerator and denominator
    num_reduced = PRODUCT_INIT
    denom_reduced = PRODUCT_INIT

    for factor in num_factors:
        
        num_reduced *= factor

    for factor in denom_factors:
        
        denom_reduced *= factor

    return [num_reduced, denom_reduced]


def reduce_fraction_arr(fract_arr: list) -> list:
    
    # Validates that the array represents a num/denom array
    if len(fract_arr) != FRACT_ARR_LEN: 
        
        return f'{fract_arr} does not represent a fraction.  Please enter an array as [numerator, denominator].'
    
    # Get unique factors of numerator and denominator
    num_factors: list = factors(fract_arr[NUM_INDEX])
    denom_factors: list = factors(fract_arr[DENOM_INDEX])

    # Remove common factors
    for factor in num_factors[:]:
        
        if factor in denom_factors:
        
            num_factors.remove(factor)
            denom_factors.remove(factor)

    # Calculate the reduced numerator and denominator
    num_reduced = PRODUCT_INIT
    denom_reduced = PRODUCT_INIT

    for factor in num_factors:
        
        num_reduced *= factor

    for factor in denom_factors:
        
        denom_reduced *= factor

    return [num_reduced, denom_reduced]
    

def slope_from_two_points(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Prevents divide by zero returns
    if x_2 == x_1: return f'Slope is undefined since x_2 = {x_2} and x_1 = {x_1}'

    return(float_quotient(difference(y_2, y_1), difference(x_2, x_1)))


def slope_from_point_array(point_arr_2: float, point_arr_1: float) -> float:

    # Validates arrays to ensure they have two coordinates:
    if len(point_arr_2) != 2 or len(point_arr_1) != 2:

        return None

    for coordinate in range(len(point_arr_2)):

        if float(point_arr_2[coordinate]) == False or float(point_arr_1[coordinate]) == False:

            return None

    return(float_quotient(difference(point_arr_2[1], point_arr_2[0]), difference(point_arr_1[1], point_arr_1[0])))


def perp_slope(slope: float) -> float:

    return neg(reciprocal(slope)) if slope != ZERO_DENOM else f'Reciprocal slope is undefined.'


def normal_slope(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    if y_2 == y_1: return f'Reciprocal slope is undefined. since y_2 = {y_2} and y_1 = {y_1}.'
    
    return neg(float_quotient(difference(x_2, x_1), difference(y_2, y_1)))

# Check it out
def slope_at_point(poly_coeff_arr: list, point_value: float) -> float:

    slope = SUM_INIT
    power = get_highest_power(poly_coeff_arr)

    for term in poly_coeff_arr:

        slope += poly_term_pt_der(poly_coeff_arr[term], point_value, power)
        power -= 1

    return slope


def midpoint_2d_arr(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Returns as a 2d ordered pair
    return [num_midpoint(x_2, x_1), num_midpoint(y_2, y_1)]


def distance_2d(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    return root(add(square_diff(x_1, x_2), square_diff(y_2, y_1)), 2)


# Verified
def general_to_vertex_quad(lead_coeff: float, linear_coeff: float, const: float, pr: bool = False) -> float:

    if lead_coeff == 0:
        
        print("Not a quadratic function when a = 0")
        return None

    calc_array = [lead_coeff, linear_coeff, const]
    horizontal_offset = float_quotient(neg(linear_coeff), double(lead_coeff))
    power = 2
    vertical_offset = 0

    
    while power >= ZEROTH_POWER:
    
        for num in range(len(calc_array)):
        
            # Debugger Line
            # print("k = ", k, "+ ", calc_array[num], " * ", h, "^", power)
            
            vertical_offset += polynomial(calc_array[num], horizontal_offset, power)
            power -= 1

    # Printing conditions for cleaner output
    
    if pr == True:
    
        horizontal_sign:str = "-" if horizontal_offset >= WHOLE_NUM_MIN else "+"
        vertical_sign:str = "+" if vertical_offset >= WHOLE_NUM_MIN else "-"
        print_hor_offset: str = str(horizontal_offset) if horizontal_offset >= WHOLE_NUM_MIN else abs_value(horizontal_offset)
        print_vert_offset: str = str(vertical_offset) if vertical_offset >= WHOLE_NUM_MIN else abs_value(vertical_offset)
        print_lead_coeff: str = str(lead_coeff) if lead_coeff != 1 else ""
        
        print("y = ", print_lead_coeff, "(x", horizontal_sign, print_hor_offset, ") ^ 2", vertical_sign, print_vert_offset)
        
    return [horizontal_offset, vertical_offset]


def quadratic_test(lead_coeff: float) -> bool:

    return False if lead_coeff == 0 else True


def calc_quad_disc(lead_coeff: float, linear_coeff: float, constant) -> float:
    
    if quadratic_test(lead_coeff) == True:

        return difference(exponentiate(linear_coeff, 2), product(4, product(lead_coeff, constant)))
        
    return f'Not a quadratic when a = {lead_coeff}'


def quad_aos(lead_coeff: float, linear_coeff: float) -> float:

    if quadratic_test(lead_coeff) == True:

        return(float_quotient(neg(linear_coeff), double( lead_coeff)))

    return f'Not a quadratic when a = {lead_coeff}'


def quad_output(lead_coeff: float, linear_coeff: float, constant: float) -> float:

    axis_of_sym = quad_aos(lead_coeff, linear_coeff)

    return add(polynomial(lead_coeff, axis_of_sym, 2), add(polynomial(linear_coeff, axis_of_sym, 1), constant))


def calc_num_ints_quad(lead_coeff: float, linear_coeff: float, constant: float) -> int:
    
    discriminant = calc_quad_disc(lead_coeff, linear_coeff, constant)

    match discriminant:

        case _ if discriminant > DISC_THRESH:

            return 2

        case _ if discriminant == DISC_THRESH:

            return 1

        case _ if discriminant < DISC_THRESH:

            return 0

        case _:

            return None


def get_aos(lead_coeff: float, linear_coeff: float, dir: str) -> str:

    
    axis_of_sym = quad_aos(lead_coeff, linear_coeff)
    
    match dir:

        case "horizontal":
        
            return f'y = {axis_of_sym}'
        
        case "vertical":
        
            return f'x = {axis_of_sym}'
        
        case _:
            
            return f'No direction specified'


def parabola_focus(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> float:

    p_value: float = reciprocal(product(4, lead_coeff))

    if dir == HOR_DIR:

        # Though it looks incorrect, we're switching inputs and outputs for the calc portion
        y_coord: float = quad_aos(lead_coeff, linear_coeff)
        x_coord: float = quad_output(lead_coeff, linear_coeff, constant)
        x_coord += p_value

    elif dir == VER_DIR:

        x_coord: float = quad_aos(lead_coeff, linear_coeff)
        y_coord: float = quad_output(lead_coeff, linear_coeff, constant)
        y_coord += p_value

    else:

        x_coord: float = None
        y_coord: float = None

    return[x_coord, y_coord]


def para_lotus_points(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> list:

    focus = parabola_focus(lead_coeff, linear_coeff, constant, dir)
    adj_value: int = reciprocal(lead_coeff)

    first_pt, second_pt = [], []

    match dir:
        
        case "vertical":
            
            first_pt: float = [difference(focus[0], adj_value), focus[1]]
            second_pt: float = [add(focus[0], adj_value), focus[1]]
        
        case "horizontal":

            first_pt: float = [focus[0], difference(focus[1], adj_value)]
            second_pt: float = [focus[0], add(focus[1], adj_value)]
        
        case _:

            raise ValueError("Invalid direction specified.")

    return [first_pt, second_pt]

# Needs work: Consider when synthetic divisors are in the form of
# ax - b, a ≠ 1 and your synthetic divisor = b/a
# Also validate situations so that a ≠ 0
# Consider entering your arguments differently as a and b instead of a synth divisor
def poly_syn_div(coeff_arr: list, synth_div: float) -> list:

    divisor = get_synth_divisor(synth_div)

    if len(coeff_arr) < 2:

        new_coeff_arr: list = []

        for coeff in coeff_arr:

            new_coeff_arr.append(float_quotient(coeff_arr[coeff], synth_div))

    # Brings down the lead coefficient
    new_coeff_arr: list = [coeff_arr[0]]

    # Moves the index of analysis over
    ind: int = 1

    while ind < range(len(coeff_arr)):

        additive: float = product(new_coeff_arr[subtract_one(ind)], synth_div)
        new_coeff_arr.append(add(coeff_arr[ind], additive))

    return new_coeff_arr


# Definitely needs to be double checked, but should be on the right track.
# Needs validation to ensure the len(remainder) ≥ len(divisor) inside loop
def poly_long_div(dividend_coeffs: list, divisor_coeffs: list) -> list:

    divisor_terms: int = get_highest_power(divisor_coeffs)
    quotient_coeffs: list = []
    new_remainder_coeffs: list = dividend_coeffs

    for dvd_coeff in range(len(dividend_coeffs)):

        product_coeffs: list = []

        quotient_coeffs.append(float_quotient(dividend_coeffs[dvd_coeff], dividend_coeffs[dvd_coeff]))

        for dvr_coeff in range(len(divisor_coeffs)):

            product_coeffs.append(product(quotient_coeffs[dvd_coeff], divisor_coeffs[dvr_coeff]))

        old_remainder_coeffs, new_remainder_coeffs = new_remainder_coeffs, []

        for prod_coeff in range(len(product_coeffs)):

            new_remainder_coeffs.append(difference(old_remainder_coeffs[prod_coeff]), product_coeffs[prod_coeff])

    return quotient_coeffs


def discrete_exponential(initial_value: float, rate: float, interval: int, power: float) -> float:

    if interval < NATURAL_NUM_MIN or int(interval) != interval:

        return f'{interval} is not valid.  Please enter a positive integer.'

    base: float = add(NATURAL_NUM_MIN, float_quotient(rate, interval))

    # Validates the domain base 
    if base <= WHOLE_NUM_MIN:
        
        return f'{base} is not a valid base for an exponential function'

    elif base == NATURAL_NUM_MIN:

        return initial_value # 1 ^ n = 1

    else: 
        
        exponent: float = product(interval, power)
        return polynomial(initial_value, base, exponent)


def continuous_exponential(initial_value: float, rate: float, power: int) -> float:

    base: float = math.e
    exponent: float = product(rate, power)

    return polynomial(initial_value, math.e, exponent)


# Needs to be tested and verified that the pop operation works as expected
def rational_zeroes_poly(num_coeff_arr: list) -> list:

    for coeff in num_coeff_arr:

        # Validates that integers are in the array only
        if num_coeff_arr[coeff] != int(num_coeff_arr[coeff]):

            return f'Rational Zeroes Theorem will not work easily with non-integers.  Please adjust your values and try again.\nProblem coeff: {num_coeff_arr[coeff]} located at index {coeff}.'

    lead_coeff: int = num_coeff_arr[0]
    constant: int = num_coeff_arr[-1]

    lead_coeff_factors: list = factors(lead_coeff) # pulled from number theory
    constant_factors: list = factors(constant)

    if len(constant_factors) == 1:

        return lead_coeff_factors

    else:

        rational_zeroes_arr: list = []

        for cf in constant_factors:

            for lcf in lead_coeff_factors:

                rational_zeroes_arr.append[float_quotient(lead_coeff_factors[lcf], constant_factors[cf])]
            
        rational_zeroes_arr.sort()

        ind = 1  # Start from 1 to avoid out-of-bounds errors

        # Get this loop checked.  Maybe .remove is better?
        while ind < len(rational_zeroes_arr): 

            if rational_zeroes_arr[ind] == rational_zeroes_arr[ind - 1]:

                rational_zeroes_arr.pop(ind)  # Remove the duplicate at the current index

            else:

                ind += 1  # Only increment `ind` if no duplicate is found

        return rational_zeroes_arr

# Testing required
# Code iterates through coefficient array at a point to calcululate result.
# Ex: [2, -3, 5] at point -1 calculates:
# 2(-1)^2 + -3(-1) + 5 which returns 10.
def calculate_poly(poly_coeffs_arr: list, point: float) -> float:

    # Initializations
    poly_sum = SUM_INIT
    power = get_highest_power(poly_coeffs_arr)

    # Go through each array and calculate the sum using the coefficient provided
    for coeff in poly_coeffs_arr:

        poly_sum += polynomial(poly_coeffs_arr[coeff], point, power)

        power -= 1

    return poly_sum

def get_synth_divisor(divisor_arr: list) -> float:

    # Looks for an array that fits ax - b = 0
    if len(divisor_arr) == 2:

        return neg(float_quotient(divisor_arr[1], divisor_arr[0])) if divisor_arr[0] != 0 else f"{divisor_arr[0]} cannot be used as an 'a' value!"

    # In the event the divisor itself is already given
    elif len(divisor_arr) == 1:

        return divisor_arr
    
    return f'Not a valid synthetic divisor!'