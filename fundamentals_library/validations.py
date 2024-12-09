from fundamentals_library.computations import *
from fundamentals_library.constants import *
import math


#VALIDATIONS

def validate_point(input_arr: list[float], num_of_dim: int) -> bool:

    if not isinstance(num_of_dim, int) or num_of_dim <= 0:

        return f'Number of dimensions must be a natural number.  Dimensions entered: {num_of_dim}.'

    if len(input_arr) != POINT_LEN_2D:
        
        return False
    
    for ind in range(len(input_arr)):

        if not isinstance(input_arr[ind], (int, float)):

            try:

                input_arr[ind] = float(input_arr[ind])

                return

            except ValueError:

                return False
            
        return True
    

def validate_numeric_list(input_arr: list) -> bool:

    if not isinstance(input_arr, list):

        return False
    
    for ind in range(len(input_arr)):

        if not isinstance(input_arr[ind], (int, float)):

            return False
        
    return True


def validate_int_list(input_arr: list) -> bool:

    if not isinstance(input_arr, list):

        return False
    
    for ind in range(len(input_arr)):

        if not isinstance(input_arr[ind], int):

            return False
        
    return True

def validate_circle_pt(test_pt_arr: list[float], vertex: list[float], radius: float) -> bool:

    # Validation of inputs:
    if not validate_point(test_pt_arr, POINT_LEN_2D) or not validate_point(vertex, POINT_LEN_2D):

        return False

    if not isinstance(radius, (int, float)):

        try:

            radius = float(radius)

        except ValueError:
        
            return f'Invalid input for radius! Please enter a numeric value.'

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