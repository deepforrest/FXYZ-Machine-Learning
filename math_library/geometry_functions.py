from fundamentals_library.computations import *
from fundamentals_library.constants import *
from math_library.number_theory import *
from math_library.differential_calculus import *
from math_library.algebraic_functions import *
import math

def length_of_line(point_one_arr: list, point_two_arr: list) -> float:

    if len(point_one_arr) != 2 or len(point_two_arr) != 2:

        return f'Point must have two dimensions.  Points given: {point_one_arr} and {point_two_arr}.'
    
    return distance_2d(point_two_arr[Y_IND], point_one_arr[Y_IND], point_two_arr[X_IND], point_one_arr[X_IND])

def angle_of_regular_n_polygon(number_of_sides: int) -> float:

    if number_of_sides < 3 or number_of_sides != int(number_of_sides):

        return f'The input {number_of_sides} does not represent a polygon.'
    
    return product((difference(number_of_sides, 2)), half(FULL_CIRCLE_DEG))

def inner_angle_n_polygon(number_of_sides: int) -> float:

    if number_of_sides < 3 or number_of_sides != int(number_of_sides):

        return f'The input {number_of_sides} does not represent a polygon.'
    
    return float_quotient(FULL_CIRCLE_DEG, number_of_sides)

def exterior_angle_n_polygon(number_of_sides: int) -> float:

    if number_of_sides < 3 or number_of_sides != int(number_of_sides):

        return f'The input {number_of_sides} does not represent a polygon.'
    
    return difference(half(FULL_CIRCLE_DEG), angle_of_regular_n_polygon(number_of_sides))

def angle_law_of_sines(corr_side: float, another_side: float, another_angle: float, angle_type: str) -> float:

    angle_used: float = another_angle if angle_type == "rad" else angle_used == product(another_angle, DEG_TO_RAD)

    return math.asin(float_quotient(product(corr_side, math.sin(another_angle)), another_side))


def side_law_of_sines(corr_angle: float, another_side: float, another_angle: float, angle_type: str) -> float:

    if angle_type == "deg":

        corr_angle *= DEG_TO_RAD
        another_angle *= DEG_TO_RAD

    return(float_quotient(product(another_side, math.sin(corr_angle)), math.sin(another_angle)))

def area_of_polygon(num_of_sides: int, len_of_side: float) -> float:

    numerator: float = polynomial(num_of_sides, len_of_side, 2)
    denominator: float = product(4, math.tan(float_quotient(half(FULL_CIRCLE_DEG), num_of_sides)))

    return float_quotient(numerator, denominator)

# Triangle Functions
def area_of_triangle(base: float, height: float) -> float:

    return half(product(base, height))

def per_of_triangle(side_a: float, side_b: float, side_c: float) -> float:

    return sum(side_a, side_b, side_c)

def find_missing_angle_rt_tri(angle: float, angle_input_type: str, angle_output_type: str) -> float:

    angle_to_analyze: float = angle

    if angle_input_type == RAD_UNIT:

        angle_to_analyze *= ANGLE_CONVERSIONS[RAD_UNIT][DEG_UNIT]

    if angle_to_analyze < RIGHT_ANGLE or angle_to_analyze > ZERO_ANGLE:

        return f'The angle {angle} is not a valid angle.'
    
    missing_angle: float = difference(RIGHT_ANGLE, angle_to_analyze)

    if angle_output_type == RAD_UNIT:

        missing_angle *= ANGLE_CONVERSIONS[DEG_UNIT][RAD_UNIT]
    
    return missing_angle

# Square Functions
def area_of_square(side_len: float) -> float:

    if side_len <= ZERO_LEN:

        return f'{side_len} is not a valid geometric input.'
    
    return squared(side_len)

def per_of_square(side_len: float) -> float:

    if side_len <= ZERO_LEN:

        return f'{side_len} is not a valid geometric input.'
    
    return product(NUM_SIDES_QUAD, side_len)

# Circle Functions
def area_of_circle(len_meas: float, len_type: str = "radius") -> float:

    if len_meas < ZERO_LEN:

        return f'{len_meas} is not a valid {len_type}.'

    calc_len: float = half(len_meas) if len_type != "radius" else len_meas

    return product(math.pi, squared(calc_len))


def validate_circle_pt(test_pt_arr: list[float], vertex: list[float], radius: float) -> bool:

    # Validation of inputs:

    if not isinstance(radius, (int, float)):

        try:

            radius = float(radius)

        except ValueError:
        
            return f'Invalid input for radius! Please enter a numeric value.'
        

    # Validates that arrays represent a 2D point [x, y]
    if len(test_pt_arr) != POINT_LEN_2D or len(vertex) != POINT_LEN_2D:

        return f'Either the test point: {test_pt_arr}, or the vertex: {vertex} is not a 2D input.  Please enter a valid input as [x, y].'
    
    # Validates that inputs for the arrays are numeric, attempts to correct them otherwise.
    for ind in test_pt_arr:

        if not isinstance(test_pt_arr[ind], (int, float)):

            try:

                test_pt_arr[ind] = float(test_pt_arr[ind])

            except ValueError:

                return f'Invalid input for the test point! Please enter numeric values.'
            
        
        if not isinstance(vertex[ind], (int, float)):

            try:

                vertex[ind] = float(vertex[ind])

            except ValueError:

                return f'Invalid input for the vertex! Please enter numeric values.'

    # Makes the radius positive, if not already.
    radius = abs_value(radius)

    # Given the input radius and test point, let's find two coordinates that work:
    y_coord_pt_vert_dist: float = difference(test_pt_arr[Y_IND], vertex[Y_IND])
    under_sqrt: float = difference(squared(radius), squared(y_coord_pt_vert_dist))

    # If the square root is negative, no further operations can be handled.
    if under_sqrt >= ZERO_LEN:

        x_coord_1: float = add(sqrt(under_sqrt), vertex[X_IND])
        x_coord_2: float = neg(x_coord_1)

        valid_pt_1: list[float] = [x_coord_1, test_pt_arr[Y_IND]]
        valid_pt_2: list[float] = [x_coord_2, test_pt_arr[Y_IND]]

        if test_pt_arr != valid_pt_1 and test_pt_arr != valid_pt_2:

            return False # Point lies inside circle
            
        return True # Point lies right on the circle
    
    return False # Point lies outside the circle