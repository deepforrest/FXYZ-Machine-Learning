from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *
from math_library.number_theory import *
from math_library.differential_calculus import *
from math_library.algebraic_functions import *
import math

def validate_shape(number_of_sides: float) -> bool:

    if number_of_sides < NUM_SIDES_TRI or not isinstance(number_of_sides, int):

        return False
    
    return True

def length_of_line(point_one_arr: list[float], point_two_arr: list[float]) -> float:

    if len(point_one_arr) != POINT_LEN_2D or len(point_two_arr) != POINT_LEN_2D:

        return f'Point must have two dimensions.  Points given: {point_one_arr} and {point_two_arr}.'
    
    return distance_2d(point_two_arr[Y_IND], point_one_arr[Y_IND], point_two_arr[X_IND], point_one_arr[X_IND])


def angle_of_regular_n_polygon(number_of_sides: int) -> float:

    if not validate_shape(number_of_sides):

        return f'The input {number_of_sides} does not represent a polygon.'
    
    return product((difference(number_of_sides, 2)), half(FULL_CIRCLE_DEG))


def inner_angle_n_polygon(number_of_sides: int) -> float:

    if not validate_shape(number_of_sides):

        return f'The input {number_of_sides} does not represent a polygon.'
    
    return float_quotient(FULL_CIRCLE_DEG, number_of_sides)


def exterior_angle_n_polygon(number_of_sides: int) -> float:

    if not validate_shape(number_of_sides):

        return f'The input {number_of_sides} does not represent a polygon.'
    
    return difference(half(FULL_CIRCLE_DEG), angle_of_regular_n_polygon(number_of_sides))


def angle_law_of_sines(corr_side: float, another_side: float, another_angle: float, angle_type: str) -> float:

    angle_used: float = another_angle if angle_type == RAD_UNIT else angle_used == product(another_angle, DEG_TO_RAD)

    return math.asin(float_quotient(product(corr_side, math.sin(another_angle)), another_side))


def side_law_of_sines(corr_angle: float, another_side: float, another_angle: float, angle_type: str) -> float:

    if angle_type == DEG_UNIT:

        corr_angle *= DEG_TO_RAD
        another_angle *= DEG_TO_RAD

    return(float_quotient(product(another_side, math.sin(corr_angle)), math.sin(another_angle)))


def area_of_polygon(num_of_sides: int, len_of_side: float) -> float:

    numerator: float = product(num_of_sides, squared(len_of_side))
    denominator: float = product(NUM_SIDES_QUAD, math.tan(float_quotient(half(FULL_CIRCLE_DEG), num_of_sides)))

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

        return f'The angle: {angle} is not a valid angle.'
    
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