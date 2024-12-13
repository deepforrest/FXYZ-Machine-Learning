from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *
from math_library.number_theory import *
from math_library.differential_calculus import *
import math

def get_intersection_arr(*arrays: list) -> list:

    # Validations
    if not arrays: return []

    # Converts an array of arrays into a single array
    if len(arrays) == LIST_OF_LISTS_LEN and isinstance(arrays[FIRST_IND], (list, tuple)):

        arrays = arrays[FIRST_IND]

    for array in arrays[:]:

        if not isinstance(array, (list, tuple)):

            try: 
                
                array = [array]

            except ValueError:

                print(f'An input: {array} could not be converted to an array. {CHECK_INPUTS}')
                return []
    
    intersection_set: set = set(arrays[FIRST_IND])

    for array in arrays[1:]:

        intersection_set.intersection_update(array)

    return list(intersection_set)


def get_intersection_c(*arrays: list) -> list:

    # Validations
    if not arrays: return []

    # Converts an array of arrays into a single array
    if len(arrays) == LIST_OF_LISTS_LEN and isinstance(arrays[FIRST_IND], (list, tuple)):

        arrays = arrays[FIRST_IND]

    validated_arrays: list = []

    for array in arrays:

        if isinstance(array, (list, tuple)):

            validated_arrays.append(list(array))

        else:

            raise ValueError(f'Input {arrays[array]} is not a valid input.  {CHECK_INPUTS}')
        
    intersection_set = set(get_intersection_arr(*arrays))
    union_set = set(get_union_arr(*arrays))

    complement_set = union_set - intersection_set

    return list(complement_set)
    

def get_union_arr(*arrays: list) -> list:

    # Validations
    if not arrays: return []

    # Converts an array of arrays into a single array
    if len(arrays) == LIST_OF_LISTS_LEN and isinstance(arrays[FIRST_IND], (list, tuple)):

        arrays = arrays[FIRST_IND]

    validated_arrays: list = []

    for array in arrays:

        if isinstance(array, (list, tuple)):

            validated_arrays.append(list(array))

        else:

            raise ValueError(f'Input {arrays[array]} is not a valid input.  {CHECK_INPUTS}')
    
    # Construction of union set
    union_set = set()

    for array in validated_arrays:

        union_set.update(array)

    return list(union_set)