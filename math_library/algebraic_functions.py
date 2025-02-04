from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *
from math_library.number_theory import *
from math_library.differential_calculus import *
import math


# Computational Theory
def reduce_fraction(num: int, denom: int) -> list[int]:

    fraction: list = [num, denom]
    # Validates the input to ensure only integers are used.

    for ind in range(len(fraction)):

        if not isinstance(fraction[ind], int):

            try:

                fraction[ind] = int(fraction[ind])

            except ValueError:

                return f'Number: {fraction[ind]} at index: {ind} was entered that is not valid.'
    
    return reduce_fraction_arr(fraction)


def reduce_fraction_arr(fract_arr: list[int]) -> list[int]:
    
    if not validate_int_list(fract_arr):

        return f'{fract_arr} contains non-int inputs and cannot be analyzed'
    
    # Validates that the array represents a num/denom array
    if len(fract_arr) != FRACT_ARR_LEN: 
        
        return f'{fract_arr} does not represent a fraction.  Please enter an array as [numerator, denominator].'
    
    # Get unique factors of numerator and denominator from number theory function.
    num_factors: list = factors(fract_arr[NUM_INDEX])
    denom_factors: list = factors(fract_arr[DENOM_INDEX])

    # Remove common factors
    for factor in num_factors[:]:
        
        if factor in denom_factors:
        
            # Cancels out common factors in numerator and denominator.
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

# Algebraic Methods (most methods have an arr counterpart)
def slope_from_two_points(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Prevents divide by zero returns
    if x_2 == x_1: return f'Slope is undefined since x_2 = {x_2} and x_1 = {x_1}.'
    
    point_1: list[float] = [x_1, y_1]
    point_2: list[float] = [x_2, y_2]

    return slope_from_points_array(point_2, point_1)


def slope_from_points_array(point_arr_2: list[float], point_arr_1: list[float]) -> float:

    # Validates arrays to ensure they have two coordinates:
    if not validate_num_arr(point_arr_2, POINT_LEN_2D) or not validate_num_arr(point_arr_1, POINT_LEN_2D):
        
        return f'Either Point 1: {point_arr_1} or Point 2: {point_arr_2} contains an invalid entry.  
        Please change to a numeric entry and try again.'

    numerator: float = difference(point_arr_2[Y_IND], point_arr_1[Y_IND])
    denominator: float = difference(point_arr_2[X_IND], point_arr_1[X_IND])

    return float_quotient(numerator, denominator)


def perp_slope(slope: float) -> float:

    return neg_recip(slope) if slope != ZERO_DENOM else f'Reciprocal slope of n/0 is undefined.'


def normal_slope_pt(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    if y_2 == y_1:

        return f'Normal line is undefined when y_2 = y_1.'
    
    point_1: list[float] = [x_1, y_1]
    point_2: list[float] = [x_2, y_2]

    return normal_slope_pt_arr(point_2, point_1)


def normal_slope_pt_arr(pt_arr_2: list[float], pt_arr_1: list[float]) -> float:

    if pt_arr_2[Y_IND] == pt_arr_1[Y_IND]:

        return 'Normal is undefined when y-coordinates are the same.'
    
    # Remember, with normals, X is on top, Y is on bottom:
    numerator: float = difference(pt_arr_2[X_IND], pt_arr_1[X_IND])
    denominator: float = difference(pt_arr_2[Y_IND], pt_arr_1[Y_IND])

    return float_quotient(neg(numerator), denominator)


def slope_at_point_poly(poly_coeff_arr: list[int], point_value: float) -> float:

    if not validate_int_list(poly_coeff_arr):

        return f'The polynomial array: {poly_coeff_arr} contains a non-numeric coefficient.'

    slope: float = SUM_INIT
    power: int = get_highest_power(poly_coeff_arr)

    for term in range(len(poly_coeff_arr)):

        slope += poly_term_pt_der(poly_coeff_arr[term], point_value, power)
        power -= 1 # Next term always reduces power by 1 in polynomials

    return slope


def midpoint_2d(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    point_1: list[float] = [x_1, y_1]
    point_2: list[float] = [x_2, y_2]

    if not validate_num_arr(point_1, POINT_LEN_2D) or not validate_num_arr(point_2, POINT_LEN_2D):

        return f'Either point 1 {point_1} or point 2 {point_2} contain non numeric values in the midpoint_2d function.
        Please fix inputs and try again.'
    
    return midpoint_2d_arr(point_2, point_1)


def midpoint_2d_arr(pt_arr_1: list[float], pt_arr_2: list[float]) -> float:

    if not validate_num_arr(pt_arr_1, POINT_LEN_2D) or not validate_num_arr(pt_arr_2, POINT_LEN_2D):

        return f'Either point 1 {pt_arr_1} or point 2 {pt_arr_2} contain non numeric values in the midpoint_2d function.
        Please fix inputs and try again.'

    x_mp_coor: float = num_midpoint(pt_arr_1[X_IND], pt_arr_2[X_IND])
    y_mp_coor: float = num_midpoint(pt_arr_1[Y_IND], pt_arr_2[Y_IND])

    # Returns as a 2d ordered pair
    return [x_mp_coor, y_mp_coor]


def distance_2d(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    point_1: list[float] = [x_1, y_1]
    point_2: list[float] = [x_2, y_2]

    if not validate_num_arr(point_1, POINT_LEN_2D) or not validate_num_arr(point_2, POINT_LEN_2D):

        return f'Either point 1 {point_1} or point 2 {point_2} contain non numeric values in the distance_2d function.
        Please fix inputs and try again.'

    return distance_2d_arr(point_2, point_1)


def distance_2d_arr(pt_arr_2: list[float], pt_arr_1: list[float]) -> float:

    if not validate_num_arr(pt_arr_1, POINT_LEN_2D) or not validate_num_arr(pt_arr_2, POINT_LEN_2D):

        return f'Either point 1 {pt_arr_1} or point 2 {pt_arr_2} contain non numeric values in the distance_2d function.
        Please fix inputs and try again.'

    x_sq_diff = square_diff(pt_arr_2[X_IND], pt_arr_1[X_IND])
    y_sq_diff = square_diff(pt_arr_2[Y_IND], pt_arr_1[Y_IND])
    sq_sum = add(x_sq_diff, y_sq_diff)

    return sqrt(sq_sum) # No need to check for domain since squaring differences makes it positive.


def general_to_vertex_quad(lead_coeff: float, linear_coeff: float, const: float, pr: bool = False) -> list[float]:

    quad_coeff_arr: list[float] = [lead_coeff, linear_coeff, const]

    # Super validation for quadratics
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None

    return general_to_vertex_quad_arr(quad_coeff_arr, pr)


def general_to_vertex_quad_arr(quad_coeff_arr: list[float], pr: bool = False) -> list[float]:

    # Super validation for quadratics
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None

    # Initializations
    hor_offset_num: float = neg(quad_coeff_arr[QUAD_LIN_COEFF_IND])
    hor_offset_den: float = double(quad_coeff_arr[QUAD_LEAD_COEFF_IND])
    horizontal_offset: float = float_quotient(hor_offset_num, hor_offset_den)

    power: int = get_highest_power(quad_coeff_arr)
    vertical_offset: float = CENTER_VERT_VAL
    
    while power >= ZEROTH_POWER:
    
        for term in range(len(quad_coeff_arr)):
        
            # Debugger Line
            # print("k = ", k, "+ ", calc_array[num], " * ", h, "^", power)
            
            vertical_offset += polynomial(quad_coeff_arr[term], horizontal_offset, power)
            power -= 1

    # Printing conditions for cleaner output
    
    if pr:
    
        horizontal_sign: str = "-" if horizontal_offset >= WHOLE_NUM_MIN else "+"
        vertical_sign: str = "+" if vertical_offset >= WHOLE_NUM_MIN else "-"
        print_hor_offset: str = str(horizontal_offset) if horizontal_offset >= WHOLE_NUM_MIN else abs_value(horizontal_offset)
        print_vert_offset: str = str(vertical_offset) if vertical_offset >= WHOLE_NUM_MIN else abs_value(vertical_offset)
        print_lead_coeff: str = str(quad_coeff_arr[QUAD_LIN_COEFF_IND]) if quad_coeff_arr[QUAD_LIN_COEFF_IND] != UNIT_COEFF else ""
        
        print("y = ", print_lead_coeff, "(x", horizontal_sign, print_hor_offset, ") ^ 2", vertical_sign, print_vert_offset)
        
    return [horizontal_offset, vertical_offset]


def calc_quad_disc(lead_coeff: float, linear_coeff: float, constant: float) -> float:
    
    quad_coeff_arr = [lead_coeff, linear_coeff, constant]

    # Super validation for quadratics
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None

    return calc_quad_disc_arr(quad_coeff_arr)
        

def calc_quad_disc_arr(quad_coeff_arr: list[float]) -> float:

    # Super validation for quadratics
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None
    
    first_term: float = squared(quad_coeff_arr[QUAD_LIN_COEFF_IND])
    second_term: float = product[AC_DISC_COEFF, quad_coeff_arr[QUAD_LEAD_COEFF_IND], quad_coeff_arr[QUAD_CONST_COEFF_IND]]

    return difference(first_term, second_term)


def quad_aos(lead_coeff: float, linear_coeff: float) -> float:

    # The constant coeff isn't really necessary, so assume it's 0
    quad_coeff_arr: list[float] = [lead_coeff, linear_coeff, ZERO_COEFF]

    # Super validation for quadratics
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None
    
    return quad_aos_arr(quad_coeff_arr)


def quad_aos_arr(quad_coeff_arr: list[float]) -> float:

    # Super validation for quadratics
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None
    
    aos_num: float = neg(quad_coeff_arr[QUAD_LIN_COEFF_IND])
    aos_denom: float = double(quad_coeff_arr[QUAD_LEAD_COEFF_IND])

    return float_quotient(aos_num, aos_denom)


def get_aos(lead_coeff: float, linear_coeff: float, dir: str) -> str:

    axis_of_sym: float = quad_aos(lead_coeff, linear_coeff)
    
    match dir:

        case "horizontal":
        
            return f'y = {axis_of_sym}'
        
        case "vertical":
        
            return f'x = {axis_of_sym}'
        
        case _:
            
            return f'No direction specified'


def quad_aos_output(lead_coeff: float, linear_coeff: float, constant: float) -> float:

    quad_arr: list[float] = [lead_coeff, linear_coeff, constant]

    return quad_aos_output_arr(quad_arr)
  

def quad_aos_output_arr(quad_coeff_arr: list[float]) -> float:
    
    # Validations
    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN):

        return None
    
    # Calculation Setup    
    axis_of_sym: float = quad_aos_arr(quad_coeff_arr)
    power: int = get_highest_power(quad_coeff_arr)

    aos_output: float = SUM_INIT

    for term in range(len(quad_coeff_arr)):

        aos_output += polynomial(quad_coeff_arr[term], axis_of_sym, power)
        power -= 1

    return aos_output


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


def parabola_focus(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> list[float]:

    quad_coeff_arr: list[float] = [lead_coeff, linear_coeff, constant]

    return parabola_focus_arr(quad_coeff_arr, dir)


def parabola_focus_arr(quad_coeff_arr: list[float], dir: str) -> list[float]:

    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None

    a_coeff: float = quad_coeff_arr[QUAD_LEAD_COEFF_IND]
    b_coeff: float = quad_coeff_arr[QUAD_LIN_COEFF_IND]
    c_coeff: float = quad_coeff_arr[QUAD_CONST_COEFF_IND]

    p_value: float = reciprocal(product(NUM_SIDES_QUAD, a_coeff))

    if dir == HOR_DIR:

        y_coord: float = quad_aos(a_coeff, b_coeff)
        x_coord: float = quad_aos_output(a_coeff, b_coeff, c_coeff)
        x_coord += p_value

    elif dir == VER_DIR:

        x_coord: float = quad_aos(a_coeff, b_coeff)
        y_coord: float = quad_aos_output(a_coeff, b_coeff, c_coeff)
        y_coord += p_value

    else:

        x_coord = None
        y_coord = None

    return[x_coord, y_coord]


def para_lotus_points(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> list[list[float]]:

    quad_coeff_arr: list[float] = [lead_coeff, linear_coeff, constant]

    return para_lotus_points_arr(quad_coeff_arr, dir)


def para_lotus_points_arr(quad_coeff_arr: list[float], dir: str) -> list[list[float]]:

    if not validate_num_arr(quad_coeff_arr, QUAD_COEFF_LEN): return None

    a_coeff: float = quad_coeff_arr[QUAD_LEAD_COEFF_IND]
    b_coeff: float = quad_coeff_arr[QUAD_LIN_COEFF_IND]
    c_coeff: float = quad_coeff_arr[QUAD_CONST_COEFF_IND]

    focus: list[float] = parabola_focus(a_coeff, b_coeff, c_coeff, dir)
    adj_value: int = reciprocal(a_coeff)

    # Give points based on direction specified:
    if dir == VER_DIR:

        x_coord_pt_1: float = difference(focus[X_IND], adj_value)
        y_coord_pt_1: float = focus[Y_IND]

        x_coord_pt_2: float = difference(focus[X_IND], neg(adj_value))
        y_coord_pt_2: float = y_coord_pt_1

    elif dir == HOR_DIR:

        x_coord_pt_1: float = focus[X_IND]
        y_coord_pt_1: float = difference(focus[Y_IND], adj_value)

        x_coord_pt_2: float = x_coord_pt_2
        y_coord_pt_2: float = difference(focus[Y_IND], neg(adj_value))

    else:

        x_coord_pt_1 = None
        y_coord_pt_1 = None

        x_coord_pt_2 = None
        y_coord_pt_2 = None


    first_pt: list[float] = [x_coord_pt_1, y_coord_pt_1]
    second_pt: list[float] = [x_coord_pt_2, y_coord_pt_2]

    return [first_pt, second_pt]

###################################################################################################
# PICK UP FROM HERE IN REVAMPS

# Needs work: Consider when synthetic divisors are in the form of
# ax - b, a ≠ 1 and your synthetic divisor = b/a
# Also validate situations so that a ≠ 0
# Consider entering your arguments differently as a and b instead of a synth divisor
def poly_syn_div(coeff_arr: list[float], synth_div: float) -> list[float]:

    divisor: float = get_synth_divisor(synth_div)

    if len(coeff_arr) < LEN_BINOMIAL_COEFFS:

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
        ind += NEXT_IND

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

# Ready for testing
def discrete_exponential(initial_value: float, rate: float, interval: int, power: float) -> float:

    base: float = add(UNIT_BASE, float_quotient(rate, interval))
    exponent: float = product(interval, power)
    
    if not validate_exponential_inputs(initial_value, base, exponent): return None

    return polynomial(initial_value, base, exponent)

# Ready for testing
def continuous_exponential(initial_value: float, rate: float, power: int) -> float:

    base: float = math.e
    exponent: float = product(rate, power)

    if not validate_exponential_inputs(initial_value, base, exponent): return None

    return polynomial(initial_value, base, exponent)


# Needs to be tested and verified that the pop operation works as expected
def rational_zeroes_poly(num_coeff_arr: list[int]) -> list[float]:

    COEFF_ARR_LEN: int = len(num_coeff_arr)

    if COEFF_ARR_LEN == SCALAR_LEN:

        return f'Please enter an array of polynomials'
    
    for coeff in range(COEFF_ARR_LEN):

        # Validates that integers are in the array only
        if num_coeff_arr[coeff] != int(num_coeff_arr[coeff]):

            return f'Rational Zeroes Theorem will not work easily with non-integers.  Please adjust your values and try again.\nProblem coeff: {num_coeff_arr[coeff]} located at index {coeff}.'

    lead_coeff: int = num_coeff_arr[FIRST_IND]
    constant: int = num_coeff_arr[LAST_IND]

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

        ind = add_one(FIRST_IND)  # Start from 1 to avoid out-of-bounds errors

        # Get this loop checked.  Maybe .remove is better?
        while ind < subtract_one(len(rational_zeroes_arr)): 

            if rational_zeroes_arr[ind] == rational_zeroes_arr[subtract_one(ind)]:

                rational_zeroes_arr.pop(ind)  # Remove the duplicate at the current index

            else:

                ind += NEXT_IND  # Only increment `ind` if no duplicate is found

        return rational_zeroes_arr

# Testing required
# Code iterates through coefficient array at a point to calcululate result.
# Ex: [2, -3, 5] at point -1 calculates:
# 2(-1)^2 + -3(-1) + 5 which returns 10.
def calculate_poly(poly_coeffs_arr: list, point: float) -> float:

    # Validations
    PCA_LEN: int = len(poly_coeffs_arr)
    if not validate_num_arr(poly_coeffs_arr, PCA_LEN): return None

    if not isinstance(point, (float, int)):

        try:

            point = float(point)

        except ValueError:

            print(f'The point entered: {point} is not a numeric entry. {CHECK_INPUTS}')
            return None

    # Initializations
    poly_sum = SUM_INIT
    power = get_highest_power(poly_coeffs_arr)

    # Go through each array and calculate the sum using the coefficient provided
    for coeff in range(PCA_LEN):

        poly_sum += polynomial(poly_coeffs_arr[coeff], point, power)

        power -= 1

    return poly_sum

def get_synth_divisor(divisor_coeff_arr: list[float]) -> float:

    if not validate_num_arr(divisor_coeff_arr, LEN_BINOMIAL_COEFFS): return None

    numerator: float = neg(divisor_coeff_arr[LAST_IND])
    denominator: float = divisor_coeff_arr[FIRST_IND]

    return float_quotient(numerator, denominator)

# Needs to be verified with the setup
def poly_multiply(poly_arr_1: list[float], poly_arr_2: list[float]) -> list[float]:

    ARR_1_LEN: int = len(poly_arr_1)
    ARR_2_LEN: int = len(poly_arr_2)

    if not validate_num_arr(poly_arr_1, ARR_1_LEN): return None 
    if not validate_num_arr(poly_arr_2, ARR_2_LEN): return None

    PROD_ARR_LEN: int = add(subtract_one(ARR_1_LEN), subtract_one(ARR_2_LEN)) # Is this necessary?
    prod_arr: list[float] = [product([FIRST_IND], add_one(PROD_ARR_LEN))]  # What does this line do again?

    for ind_1, coeff_1 in enumerate(poly_arr_1):

        for ind_2, coeff_2 in enumerate(poly_arr_2):

            prod_arr[add(ind_1, ind_2)] += product(coeff_1, coeff_2)

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


# Needs validation.  What does binomial_arr represent?
def calc_binomial_term(binomial_arr: list[float], kth_term: int, nth_exp: int) -> float:

    if not isinstance(kth_term, int) or not isinstance(nth_exp, int): return None
    if len(binomial_arr) != POINT_LEN_2D: return None

    bin_coeff: int = binomial_coeff(kth_term, nth_exp)
    bin_first_term: float = exponentiate(binomial_arr[FIRST_IND], difference(nth_exp, kth_term))
    bin_sec_term: float = exponentiate(binomial_arr[LAST_IND], kth_term)

    return product[bin_coeff, bin_first_term, bin_sec_term]


def output_of_poly_function(poly_coeff_arr: list[float], input: float) -> float:

    for coeff in range(len(poly_coeff_arr)):

        if not isinstance(poly_coeff_arr[coeff], (int, float)):

            try:

                poly_coeff_arr[coeff] = float(poly_coeff_arr)

            except ValueError:

                return f'Input {poly_coeff_arr[coeff]} within index {coeff} is not a valid input! Please use numbers and try again'
        
        power = get_highest_power(poly_coeff_arr)
        output = SUM_INIT

        for coeff in poly_coeff_arr:

            output += polynomial(poly_coeff_arr[coeff], input, power)
            power -= 1

        return output

def validate_pt_on_poly(poly_coeff_arr: list[float], input: float, test_pt: list[float]) -> bool:

    # Array Validations
    if not validate_num_arr(test_pt, POINT_LEN_2D): return None
    if not validate_num_arr(poly_coeff_arr, len(poly_coeff_arr)): return None

    # Calculations for comparison
    expected_output: float = output_of_poly_function(poly_coeff_arr, input)

    if expected_output != test_pt[Y_IND]:

        return False # Different outputs
    
    return True # Same outputs

def solve_abs_eq(algebraic_arr: list[float], rhs_target: float) -> list[float]:

    if not validate_alg_list(algebraic_arr): return None

    # algebraic constants for a|b(x-h)| + k = rhs
    a = algebraic_arr[A_IND]
    b = algebraic_arr[B_IND]
    h = algebraic_arr[H_IND]
    k = algebraic_arr[K_IND]

    if (a > ZERO_COEFF and rhs_target < k) or (a < ZERO_COEFF and rhs_target > k):

        print("No solutions")
        return None

    if rhs_target == k:

        return h

    numerator: float = difference(rhs_target, k)
    denominator: float = product(a, b)

    second_term = float_quotient(numerator, denominator)

    sol_1 = add(h, second_term)
    sol_2 = add(h, neg(second_term))

    return [sol_1, sol_2]


def flip_on_x_axis(algebraic_arr: list[float]) -> list[float]:

    if not validate_alg_list(algebraic_arr): return None

    new_arr: list[float] = algebraic_arr
    new_arr[A_IND] = neg(new_arr[A_IND])

    return new_arr


def flip_on_y_axis(algebriac_arr: list[float]) -> list[float]:

    if not validate_alg_list(algebriac_arr): return None

    new_arr: list[float] = algebriac_arr
    new_arr[B_IND] = neg(new_arr[B_IND])

    return new_arr


def hor_trans_arr(algebraic_arr: list[float], hor_units: float) -> list[float]:

    if not validate_alg_list(algebraic_arr): return None

    if not isinstance(hor_units, (int, float)):

        try:

            hor_units = float(hor_units)

        except ValueError:

            print(f'The horizontal units entered: {hor_units} is not a number and cannot be processed. {CHECK_INPUTS}.')
            return None

    new_arr: list[float] = algebraic_arr
    new_arr[H_IND] += hor_units

    return new_arr


def ver_trans_arr(algebraic_arr: list[float], ver_units: float) -> float:

    if not validate_alg_list(algebraic_arr): return None

    if not isinstance(ver_units, (int, float)):

        try:

            ver_units = float(ver_units)

        except ValueError:

            print(f'The vertical units entered: {ver_units} is not a number and cannot be processed. {CHECK_INPUTS}.')
            return None

    new_arr: list[float] = algebraic_arr
    new_arr[K_IND] += ver_units

    return new_arr

def calculate_algebraic_pt(algebraic_arr: list[float], pt: float, power: float) -> float:

    # Validations
    if not validate_alg_list(algebraic_arr): return None

    if not isinstance(pt, (int, float)):

        try:

            pt = float(pt)

        except ValueError:

            print(f'The point entered: {pt} is not a number and cannot be processed. {CHECK_INPUTS}.')
            return None
        
    if not isinstance(power, (int, float)):

        try:

            power = float(power)

        except ValueError:

            print(f'The power entered: {power} is not a number and cannot be processed. {CHECK_INPUTS}.')
            return None

    # Calculations (Progressive build using Order of Operations)
    pt_output: float = difference(pt, algebraic_arr[H_IND]) # (x - h)
    pt_output *= algebraic_arr[B_IND] # b(x - h)
    pt_output = exponentiate(pt_output, power) # (b(x - h))^n
    pt_output *= algebraic_arr[A_IND] # a(b(x - h))^n
    pt_output += algebraic_arr[K_IND] # a(b(x - h))^n + k

    return pt_output

# Creates an exponential function of ab^x
def exp_function_arr(pt_1_arr: list[float], pt_2_arr: list[float]) -> list[float]:

    diff_x:float = difference(pt_1_arr[X_IND], pt_2_arr[X_IND])
    exponent:float = reciprocal(diff_x)
    y_ratio:float = float_quotient(pt_1_arr[Y_IND], pt_2_arr[Y_IND])

    base: float = exponentiate(y_ratio, exponent)

    lc_denom: float = exponentiate(base, pt_1_arr[X_IND])

    lead_coeff: float = float_quotient(pt_1_arr[Y_IND], lc_denom)

    return [lead_coeff, base]

# Only works for integer outputs, needs testing.
def log(base: float, number: float) -> float:

    if not validate_log_inputs(base, number): return None

    test_num: float = number
    result = SUM_INIT

    while test_num > 1:

        # Do some division here to add to the result
        number /= base
        result += 1

    return result