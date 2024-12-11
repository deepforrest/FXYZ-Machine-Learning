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


def validate_num_arr(quad_coeff_arr: list[float], expected_len: int, function_name: str = "") -> bool:

    # Validation Algebra: A ^ B ^ C ^ D ^ E
    #1: Checks expected length to ensure it's a natural number
    if not isinstance(expected_len, int) or expected_len <= NATURAL_NUM_MIN:

        print(f'The expected length to be verified is not a natural number.  Please enter a positive nonzero integer and try again.')
        
        return False

    #2: Check to make sure the array is a list
    if not isinstance(quad_coeff_arr, list):

        print(f'The input array: {quad_coeff_arr} is not an array and cannot be used in a numeric list validation.  {CHECK_INPUTS}')

        return False

    #3: Ensures the length of the list matches the target
    if len(quad_coeff_arr) != expected_len:

        print(f'The array entered {quad_coeff_arr} did not have a length of {expected_len} as expected in the {function_name} function.  {CHECK_INPUTS}')

        return False
    
    #4: Rejects a list with a lead coeff of zero
    if quad_coeff_arr[FIRST_IND] == ZERO_COEFF:

        print(f'The array entered contains a zero lead coeff when called in the {function_name} function.  {CHECK_INPUTS}')

        return False
    
    #5: Checks each coeff to ensure it's a number
    for coeff in range(len(quad_coeff_arr)):

        if not isinstance(quad_coeff_arr[coeff], (int, float)):

            print(f'The array entered {quad_coeff_arr} has a non-numeric entry at index {coeff} when called in the {function_name}. {CHECK_INPUTS}')
            
            return False
    
    # Returns True when it passes all validations.
    return True


def validate_exponential_inputs(initial_value: float, base: float, power: float) -> bool:

    # Validation Algebra: A ^ B
    #1: Validates that inputs are all numbers:
    num_arr: list[float] = [initial_value, base, power]

    for ind in range(len(num_arr)):

        if not isinstance(num_arr[ind], (int, float)):

            print(f'The entry {num_arr[ind]} at index {ind} is not a valid input in array [initial_value, base, power]. {CHECK_INPUTS}')
            
            return False

    #2: Validates the base as a positive, non-zero and non-unit (1) base.
    if base <= ZERO_BASE or base == UNIT_BASE:

        print(f'The base entered: {base} must be a positive, nonzero, and non-unit base (≠ 1). Base domain: (0, 1) U (1, inf). {CHECK_INPUTS}')

        return False
    
    return True