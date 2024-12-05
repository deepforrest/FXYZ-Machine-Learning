from fundamentals_library.computations import *
from fundamentals_library.constants import *
from math_library.number_theory import *
from math_library.differential_calculus import *
import math

def reduce_fraction(num: int, denom: int) -> list[int]:
    # Get unique factors of numerator and denominator
    num_factors: list[int] = factors(num)
    denom_factors: list[int] = factors(denom)

    # Remove common factors
    for factor in num_factors[:]:
        
        if factor in denom_factors:
        
            num_factors.remove(factor)
            denom_factors.remove(factor)

    # Calculate the reduced numerator and denominator
    num_reduced: int = PRODUCT_INIT
    denom_reduced: int = PRODUCT_INIT

    for factor in num_factors:
        
        num_reduced *= factor

    for factor in denom_factors:
        
        denom_reduced *= factor

    return [num_reduced, denom_reduced]


def reduce_fraction_arr(fract_arr: list[int]) -> list[int]:
    
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
    num_reduced: int = PRODUCT_INIT
    denom_reduced: int = PRODUCT_INIT

    for factor in num_factors:
        
        num_reduced *= factor

    for factor in denom_factors:
        
        denom_reduced *= factor

    return [num_reduced, denom_reduced]


def reduce_fraction_arr(fract_arr: list[int]) -> list[int]:
    
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

    return float_quotient(difference(y_2, y_1), difference(x_2, x_1))


def slope_from_point_array(point_arr_2: float, point_arr_1: float) -> float:

    # Validates arrays to ensure they have two coordinates:
    if len(point_arr_2) != POINT_LEN_2D or len(point_arr_1) != POINT_LEN_2D:

        return None

    for coordinate in range(len(point_arr_2)):

        if not float(point_arr_2[coordinate]) or not float(point_arr_1[coordinate]):

            return None

    return float_quotient(difference(point_arr_2[1], point_arr_2[0]), difference(point_arr_1[1], point_arr_1[0]))


def perp_slope(slope: float) -> float:

    return neg(reciprocal(slope)) if slope != ZERO_DENOM else f'Reciprocal slope is undefined.'


def normal_line(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    if y_2 == y_1: return f'Reciprocal slope is undefined. since y_2 = {y_2} and y_1 = {y_1}.'
    
    return neg(float_quotient(difference(x_2, x_1), difference(y_2, y_1)))

# Check it out
def slope_at_point(poly_coeff_arr: list[int], point_value: float) -> float:

    slope: float = SUM_INIT
    power: int = get_highest_power(poly_coeff_arr)

    for term in range(len(poly_coeff_arr)):

        slope += poly_term_pt_der(poly_coeff_arr[term], point_value, power)
        power -= 1

    return slope


def midpoint_2d_arr(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Returns as a 2d ordered pair
    return [num_midpoint(x_2, x_1), num_midpoint(y_2, y_1)]


def distance_2d(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    x_sq_diff = square_diff(x_2, x_1)
    y_sq_diff = square_diff(y_2, y_1)
    sq_sum = add(x_sq_diff, y_sq_diff)

    return root(sq_sum, 2)


# Verified
def general_to_vertex_quad(lead_coeff: float, linear_coeff: float, const: float, pr: bool = False) -> float:

    if lead_coeff == 0:
        
        print("Not a quadratic function when a = 0")
        return None

    calc_array: list[int] = [lead_coeff, linear_coeff, const]
    horizontal_offset: float = float_quotient(neg(linear_coeff), double(lead_coeff))
    power: int = 2
    vertical_offset: float = 0

    
    while power >= ZEROTH_POWER:
    
        for num in range(len(calc_array)):
        
            # Debugger Line
            # print("k = ", k, "+ ", calc_array[num], " * ", h, "^", power)
            
            vertical_offset += polynomial(calc_array[num], horizontal_offset, power)
            power -= 1

    # Printing conditions for cleaner output
    
    if pr:
    
        horizontal_sign: str = "-" if horizontal_offset >= WHOLE_NUM_MIN else "+"
        vertical_sign: str = "+" if vertical_offset >= WHOLE_NUM_MIN else "-"
        print_hor_offset: str = str(horizontal_offset) if horizontal_offset >= WHOLE_NUM_MIN else abs_value(horizontal_offset)
        print_vert_offset: str = str(vertical_offset) if vertical_offset >= WHOLE_NUM_MIN else abs_value(vertical_offset)
        print_lead_coeff: str = str(lead_coeff) if lead_coeff != 1 else ""
        
        print("y = ", print_lead_coeff, "(x", horizontal_sign, print_hor_offset, ") ^ 2", vertical_sign, print_vert_offset)
        
    return [horizontal_offset, vertical_offset]


def quadratic_test(lead_coeff: float) -> bool:

    return False if lead_coeff == 0 else True


def calc_quad_disc(lead_coeff: float, linear_coeff: float, constant: float) -> float:
    
    if quadratic_test(lead_coeff):

        return difference(squared(linear_coeff), product(4, product(lead_coeff, constant)))
        
    return f'Not a quadratic when a = {lead_coeff}'


def quad_aos(lead_coeff: float, linear_coeff: float) -> float:

    if quadratic_test(lead_coeff):

        return float_quotient(neg(linear_coeff), double(lead_coeff))

    return f'Not a quadratic when a = {lead_coeff}.'


def quad_aos_output(lead_coeff: float, linear_coeff: float, constant: float) -> float:

    axis_of_sym: float = quad_aos(lead_coeff, linear_coeff)
    quad_arr: list[float] = [lead_coeff, linear_coeff, constant]
    power: int = get_highest_power(quad_arr)

    output_coord: float = SUM_INIT

    for coeff in range(len(quad_arr)):

        output_coord += polynomial(quad_arr[coeff], axis_of_sym, power)
        power -= 1

    return output_coord


def calc_num_ints_quad(lead_coeff: float, linear_coeff: float, constant: float) -> int:
    
    discriminant: float = calc_quad_disc(lead_coeff, linear_coeff, constant)

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

    axis_of_sym: float = quad_aos(lead_coeff, linear_coeff)
    
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

        y_coord: float = quad_aos(lead_coeff, linear_coeff)
        x_coord: float = quad_aos_output(lead_coeff, linear_coeff, constant)
        x_coord += p_value

    elif dir == VER_DIR:

        x_coord: float = quad_aos(lead_coeff, linear_coeff)
        y_coord: float = quad_aos_output(lead_coeff, linear_coeff, constant)
        y_coord += p_value

    else:

        x_coord: float = None
        y_coord: float = None

    return[x_coord, y_coord]


def para_lotus_points(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> list:

    focus: float = parabola_focus(lead_coeff, linear_coeff, constant, dir)
    adj_value: int = reciprocal(lead_coeff)

    first_pt: list[float] = []
    second_pt: list[float] = []

    match dir:
        
        case "vertical":
            
            first_pt: float = [difference(focus[0], adj_value), focus[1]]
            second_pt: float = [add(focus[0], adj_value), focus[1]]
        
        case "horizontal":

            first_pt: float = [focus[0], difference(focus[1], adj_value)]
            second_pt: float = [focus[0], add(focus[1], adj_value)]
        
        case _:

            raise ValueError("Invalid direction specified.")
            return None

    return [first_pt, second_pt]

# Needs work: Consider when synthetic divisors are in the form of
# ax - b, a ≠ 1 and your synthetic divisor = b/a
# Also validate situations so that a ≠ 0
# Consider entering your arguments differently as a and b instead of a synth divisor
def poly_syn_div(coeff_arr: list[float], synth_div: float) -> list[float]:

    divisor: float = get_synth_divisor(synth_div)

    if len(coeff_arr) < 2:

        new_coeff_arr: list[float] = []

        for coeff in coeff_arr:

            new_coeff_arr.append(float_quotient(coeff_arr[coeff], synth_div))

    # Brings down the lead coefficient
    new_coeff_arr: list[float] = [coeff_arr[0]]

    # Moves the index of analysis over
    ind: int = 1

    while ind < range(len(coeff_arr)):

        additive: float = product(new_coeff_arr[subtract_one(ind)], synth_div)
        new_coeff_arr.append(add(coeff_arr[ind], additive))

    return new_coeff_arr


# Definitely needs to be double checked, but should be on the right track.
# Needs validation to ensure the len(remainder) ≥ len(divisor) inside loop
def poly_long_div(dividend_coeffs: list[float], divisor_coeffs: list[float]) -> list[float]:

    divisor_terms: int = get_highest_power(divisor_coeffs)
    quotient_coeffs: list[float] = []
    new_remainder_coeffs: list[float] = dividend_coeffs

    for dvd_coeff in range(len(dividend_coeffs)):

        product_coeffs: list[float] = []

        quotient_coeffs.append(float_quotient(dividend_coeffs[dvd_coeff], dividend_coeffs[dvd_coeff]))

        for dvr_coeff in range(len(divisor_coeffs)):

            product_coeffs.append(product(quotient_coeffs[dvd_coeff], divisor_coeffs[dvr_coeff]))

        # Swaps the lists
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

        return initial_value # k * (1 ^ n) = k

    else: 
        
        exponent: float = product(interval, power)
        return polynomial(initial_value, base, exponent)


def continuous_exponential(initial_value: float, rate: float, power: int) -> float:

    base: float = math.e
    exponent: float = product(rate, power)

    return polynomial(initial_value, math.e, exponent)


# Needs to be tested and verified that the pop operation works as expected
def rational_zeroes_poly(num_coeff_arr: list) -> list:

    if len(num_coeff_arr) == SCALAR_LEN:

        return f'Please enter an array of polynomials'
    
    for coeff in range(len(num_coeff_arr)):

        # Validates that integers are in the array only
        if num_coeff_arr[coeff] != int(num_coeff_arr[coeff]):

            return f'Rational Zeroes Theorem will not work easily with non-integers.  Please adjust your values and try again.\nProblem coeff: {num_coeff_arr[coeff]} located at index {coeff}.'

    lead_coeff: int = num_coeff_arr[0]
    constant: int = num_coeff_arr[-1]

    lead_coeff_factors: list[float] = factors(lead_coeff) # pulled from number theory
    constant_factors: list[float] = factors(constant)

    if len(constant_factors) == SCALAR_LEN:

        return lead_coeff_factors

    else:

        rational_zeroes_arr: list[float] = []

        for cf in range(len(constant_factors)):

            for lcf in range(len(lead_coeff_factors)):

                rational_zeroes_arr.append[float_quotient(lead_coeff_factors[lcf], constant_factors[cf])]
            
        rational_zeroes_arr.sort()

        ind = 1  # Start from 1 to avoid out-of-bounds errors

        # Get this loop checked.  Maybe .remove is better?
        while ind < subtract_one(len(rational_zeroes_arr)): 

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
    for coeff in range(len(poly_coeffs_arr)):

        poly_sum += polynomial(poly_coeffs_arr[coeff], point, power)

        power -= 1

    return poly_sum

def get_synth_divisor(divisor_arr: list[float]) -> float:

    # Looks for an array that fits ax - b = 0
    if len(divisor_arr) == 2:

        return neg(float_quotient(divisor_arr[1], divisor_arr[0])) if divisor_arr[0] != ZERO_DENOM else f"{divisor_arr[0]} cannot be used as an 'a' value!"

    # In the event the divisor itself is already given
    elif len(divisor_arr) == SCALAR_LEN:

        return divisor_arr
    
    return f'Not a valid synthetic divisor!'


def poly_multiply(poly_arr_1: list[float], poly_arr_2: list[float]) -> list[float]:

    prod_arr_len: int = len(poly_arr_1) + len(poly_arr_2) - 2
    prod_arr: list[float] = product([0], add_one(prod_arr_len))

    for ind_1, coeff_1 in enumerate(poly_arr_1):

        for ind_2, coeff_2 in enumerate(poly_arr_2):

            prod_arr[ind_1 + ind_2] += product(coeff_1, coeff_2)

    return prod_arr

# Example List: [1, 0, 3, 0]
def odd_function_test_arr(poly_arr: list[float]) -> bool:

    # Check to see the number of terms.  Odd polynomial arrays must have an even length
    if remainder(len(poly_arr), 2) != 0:

        return False

    # Used for countdown
    poly_deg = get_highest_power(poly_arr)

    for coeff in range(len(poly_arr)):

        # Checks to see if the term is part of the even section and if its coefficient is 0 or not.
        if remainder(poly_deg, 2) == 0 and poly_arr[coeff] != 0: return False
            
        poly_deg -= 1

    return True

def even_function_test_arr(poly_arr: list[float]) -> bool:

    # Check to see the number of terms.  Even polynomial arrays must have an odd length: [1, 0 , -4] => x^2 - 4
    if remainder(len(poly_arr), 2) == 0:

        return False

    # Used for countdown
    poly_deg = get_highest_power(poly_arr)

    for coeff in range(len(poly_arr)):

        # Checks to see if the term is part of the odd section and if its coefficient is 0 or not.
        if remainder(poly_deg, 2) != 0 and poly_arr[coeff] != 0: return False
            
        poly_deg -= 1

    return True

def odd_or_even_poly_arr(poly_arr: list[float]) -> str:

    odd_test: bool = odd_function_test_arr(poly_arr)
    even_test: bool = even_function_test_arr(poly_arr)

    if odd_test:

        return f'{poly_arr} is an odd function.'

    elif even_test:

        return f'{poly_arr} is an even function.'

    else:

        return f'{poly_arr} is neither odd or even.'

def binomial_coeff(kth_term: int, nth_exponent) -> int:

    # Switches the numbers if entered out order
    if nth_exponent > kth_term:

        nth_exponent, kth_term = kth_term, nth_exponent

    return float_quotient(factorial(nth_exponent), product(factorial(kth_term), factorial(difference(nth_exponent - kth_term))))

def calc_binomial_term(binomial_arr: list[float], kth_term: int, nth_exp: int) -> float:

    if not int(kth_term) or not int(nth_exp): return None

    k: int = binomial_coeff(kth_term, nth_exp)
    bin_first_term: float = binomial_arr[0]
    bin_sec_term: float = binomial_arr[1]

    result = [k, exponentiate(bin_first_term, difference(nth_exp, kth_term)), exponentiate(bin_sec_term, kth_term)]

    return product(result)