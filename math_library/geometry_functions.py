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
    denominator: float = product(4, math.tan(half(FULL_CIRCLE_DEG), num_of_sides))

    return float_quotient(numerator, denominator)