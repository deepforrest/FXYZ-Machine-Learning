from math import *
from math_library.fund_comp import *
from fundamentals_library.constants import *

def reduce_fraction(num: int, denom: int) -> int:

    # Function Steps:
    #! Determine all factors of numerator and denomonator
    #! Go through both arrays and cancel out factors
    # Multiply remaining factors together
    # Return an array with reduce numerator and denominator

    # Stage 1: Get Factors
    num_to_reduce: int = num
    denom_to_reduce: int = denom

    num_factors = []
    denom_factors = []

    # Stage 2: ???

    # Stage 3: Create Reduced Numbers
    reduced_num = PRODUCT_INIT
    reduced_denom = PRODUCT_INIT

    if range(len(num_factors)) == range(len(denom_factors)):

        for i in num_factors:

            reduced_num *= num_factors[i]
            reduced_denom *= denom_factors[i]

        return [reduced_num, reduced_denom]

    else: 

        for i in num_factors:

            reduced_num *= num_factors[i]

        for i in denom_factors:

            reduced_denom *= denom_factors[i]

        return [reduced_num, reduced_denom]

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