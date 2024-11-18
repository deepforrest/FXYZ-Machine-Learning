from fundamentals_library.constants import *

# Function 01 Family: Elementary Functions
# These functions were created to remove the clutter of +, -, *, and / operations to make them more readable and intentional.  This also prevents mismatched parentheses in most cases.
# Current number of functions: 9

# Function 01-001
def add(first_num: float, second_num: float) -> float:

    return first_num + second_num


# Function 01-002
def difference(first_num: float, second_num: float) -> float:

    return first_num - second_num


# Function 01-003
def product(first_num: float, second_num: float) -> float:

    return first_num * second_num


# Function 01-004
# This function will likely need to be updated to handle indeterminant forms.
def float_quotient(num: float, denom: float) -> float:

    return num / denom if denom != ZERO_DENOM else None


# Function 01-005
# This function will likely need to be updated to handle indeterminant forms.
def int_quotient(num: float, denom: float) -> int:

    # // means integer division
    return num // denom if denom != ZERO_DENOM else None


# Function 01-006
# This function may need more checks to ensure the wrong data type is not passed.
def remainder(num: float, denom: float) -> int:

    return num % denom if denom != ZERO_DENOM else None


# Function 01-007
def exponentiate(base: float, power: float) -> float:

    if base != ZERO_BASE:

        if power!= ZEROTH_POWER:
        
            return base ** power
        
        return ZERO_BASE
    
    return None

#Function 01-008
def root(base: float, nth_root: float) -> float:

    # Calls Functions 01-007, ######, & 
    return exponentiate(base, reciprocal(nth_root))

def sci_note(power: int) -> float:

    return exponentiate(SCI_BASE, power)

# Part II: Advanced Math Functions, Nonarray

def neg(num: float) -> float:

    return -num


def reciprocal(num: float) -> float:

    return float_quotient(1, num) if num != ZERO_DENOM else None


def abs_value(num: float) -> float:

    return num if num >= WHOLE_NUM_MIN else neg(num)


def add_one(num):

    return add(num, 1)


def subtract_one(num):

    return difference(num, 1)


def polynomial(coeff: float, base: float, power: float) -> float:

    return product(coeff, exponentiate(base, power))


def num_midpoint(first_num: float, second_num: float) -> float:

    return float_quotient(add(first_num, second_num), 2)


def factorial(num: int) -> int:

    if num >= WHOLE_NUM_MIN and int(num) == True:

        result = PRODUCT_INIT
        counter = num

        while counter > NATURAL_NUM_MIN:

            result *= counter
            counter -= 1

        return result

    return None


def polynomial_derivative(coeff: float, base: float, power: float) -> float:

    # Checks for instances of divide by 0 and/or indeterminant forms
    if power <= ZEROTH_POWER and base == ZERO_BASE:
        
        return None

    return polynomial(product(coeff, power), base, subtract_one(power))


def product_op(num_start: int, num_finish: int) -> int:

    # Validates that numbers are starting from low to high, switches them if needed.
    input_start = num_start if num_start <= num_finish else num_finish
    input_finish = num_finish if num_finish >= num_start else num_start
    
    return float_quotient(factorial(input_finish), factorial(input_start))


# Part III: Algebra I Calculations

def slope_from_two_points(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Prevents divide by zero returns
    if x_2 == x_1: return None

    return(float_quotient(difference(y_2, y_1), difference(x_2, x_1)))


# Ready To Test
def slope_from_point_array(point_arr_2: float, point_arr_1: float) -> float:

    # Validates arrays to ensure they have two coordinates:
    if len(point_arr_2) != 2 and len(point_arr_1) != 2:

        return None

    for coordinate in range(len(point_arr_2)):

        if float(point_arr_2[coordinate]) == False or float(point_arr_1[coordinate]) == False:

            return None

    return(float_quotient(difference(point_arr_2[1], point_arr_2[0]), difference(point_arr_1[1], point_arr_1[0])))


def perp_slope(slope: float) -> float:

    return neg(reciprocal(slope)) if slope != ZERO_DENOM else None


def normal_slope(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    if y_2 == y_1:

        return None
    
    return neg(float_quotient(difference(x_2, x_1), difference(y_2, y_1)))

# Needs to be thought out
#def slope_at_point(poly_coeff_arr: List[float]):
#
#   return -1


def midpoint_2d_arr(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Returns as a 2d ordered pair
    return [num_midpoint(x_2, x_1), num_midpoint(y_2, y_1)]


def distance_2d(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    return root(add(exponentiate(difference(x_1, x_2), 2), (exponentiate(difference(y_1, y_2), 2))), 2)


def general_to_vertex_quad(lead_coeff: float, linear_coeff: float, const: float) -> float:

    if lead_coeff == 0:
        
        print("Not a quadratic function when a = 0")
        return None

    calc_array = [lead_coeff, linear_coeff, const]
    horizontal_offset = float_quotient(neg(linear_coeff), product(2, lead_coeff))
    power = 2
    vertical_offset = 0

    
    while power >= ZEROTH_POWER:
    
        for num in range(len(calc_array)):
        
            # Debugger Line
            # print("k = ", k, "+ ", calc_array[num], " * ", h, "^", power)
            
            vertical_offset += polynomial(calc_array[num], horizontal_offset, power)
            power -= 1

    # Printing conditions for cleaner output
    
    horizontal_sign = "-" if horizontal_offset >= WHOLE_NUM_MIN else "+"
    vertical_sign = "+" if vertical_offset >= WHOLE_NUM_MIN else "-"
    print_hor_offset: str = str(horizontal_offset) if horizontal_offset >= WHOLE_NUM_MIN else abs_value(horizontal_offset)
    print_vert_offset: str = str(vertical_offset) if vertical_offset >= WHOLE_NUM_MIN else abs_value(vertical_offset)
    print_lead_coeff: str = str(lead_coeff) if lead_coeff != 1 else ""
    
    print("y = ", print_lead_coeff, "(x", horizontal_sign, print_hor_offset, ") ^ 2", vertical_sign, print_vert_offset)
    
    return [horizontal_offset, vertical_offset]

# Discrete Math Terms

def nth_term_arith(first_term: float, nth_rank: int, common_diff: float) -> float:

    return add(first_term, product(subtract_one(nth_rank), common_diff))


def nth_term_geo(first_term: float, nth_rank: int, common_ratio) -> float:

    return polynomial(first_term, common_ratio, subtract_one(nth_rank))


def find_comm_diff(first_term: float, nth_term: float, nth_rank: int) -> float:

    if int(nth_rank) == False or nth_rank < 2:

        return None

    return float_quotient(difference(nth_term, first_term), subtract_one(nth_rank))


def find_first_term_arith(nth_term: float, nth_rank: float, common_diff: float) -> float:

    return difference(nth_term, subtract_one(nth_rank))


def arith_sum(num_terms: int, first_term: float, last_term: float) -> float:

    return float_quotient(product(num_terms, add(first_term, last_term)), 2)


def geo_sum_part(num_terms: float, nth_term: int, common_ratio: float) -> float:

    return float_quotient(difference(1, exponentiate(common_ratio, nth_term)), difference(1, common_ratio))


def geo_sum_inf(common_ratio: float, first_term: float) -> float:

    # Note that the common_ratio must be between -1 and +1, exclusive.
    return float_quotient(first_term, difference(1, common_ratio)) if abs_value(common_ratio) < 1 else None

# Part X: Test Functions


def mult_then_divide(num_times: int):

    counter: int = 1
    numerator: int = 1
    denominator: int = 1
    no_remainder: int = 0

    while counter <= num_times:

        # Hopefully Python will allow ternary expressions with multiple variable :-/
        
        if counter % 2 == no_remainder:
        
            numerator *= counter
        
        else:
        
            denominator *= counter

        counter += 1
    
    # print(numerator, " / ", denominator, " = ", str(numerator/denominator))
    return numerator/denominator


def calc_quad_disc(lead_coeff: float, linear_coeff: float, constant) -> float:

    return difference(exponentiate(linear_coeff, 2), product(4, product(lead_coeff, constant)))


def calc_x_vertex(lead_coeff: float, linear_coeff: float) -> float:

    return(float_quotient(neg(linear_coeff), product(2, lead_coeff)))


def calc_y_vertex(lead_coeff: float, linear_coeff: float, constant: float):

    x_vertex = calc_x_vertex(lead_coeff, linear_coeff)

    return add(polynomial(lead_coeff, x_vertex, 2), add(polynomial(linear_coeff, x_vertex, 1), constant))


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


def axis_of_sym(coord: float, dir: str) -> str:

    match dir:

        case "horizontal":
        
            return f'y = {coord}'
        
        case "vertical":
        
            return f'x = {coord}'
        
        case _:
            
            return f'No direction specified'



def parabola_focus(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> float:

    x_coord: float = calc_x_vertex(lead_coeff, linear_coeff, constant)
    
    y_coord: float = calc_y_vertex(lead_coeff, linear_coeff, constant)

    p_value: float = reciprocal(product(4, lead_coeff))

    if dir == "horizontal":

        x_coord += p_value

    if dir == "vertical":

        y_coord += p_value

    return[x_coord, y_coord]


def para_lotus_points(lead_coeff: float, linear_coeff: float, constant: float, dir: str) -> list:

    focus = parabola_focus(lead_coeff, linear_coeff, constant, dir)
    adj_value: int = reciprocal(lead_coeff)

    first_pt, second_pt = [], []

    match dir:
        
        case "vertical":
            
            first_pt: float = [focus[0] - adj_value, focus[1]]
            second_pt: float = [focus[0] + adj_value, focus[1]]
        
        case "horizontal":

            first_pt: float = [focus[0], focus[1] - adj_value]
            second_pt: float = [focus[0], focus[1] + adj_value]
        
        case _:

            raise ValueError("Invalid direction specified")

    return [first_pt, second_pt]


def syn_div(coeff_arr: float, synth_div: float) -> float:

    if len(coeff_arr) < 2: return None

    new_coeff_arr = [coeff_arr[0]]
    ind = 1

    while ind < range(len(coeff_arr)):

        additive = product(new_coeff_arr[ind - 1], synth_div)
        new_coeff_arr.append(add(coeff_arr[ind], additive))

    return new_coeff_arr


def div_then_mult_num(num: int) -> int:

    to_divide: bool = True
    counter: int = num
    final_num: int = num

    while counter > NATURAL_NUM_MIN:

        counter -= 1
        
        if to_divide == True:

            final_num /= counter
            to_divide == False

        else:

            final_num *= counter
            to_divide == True

    return final_num