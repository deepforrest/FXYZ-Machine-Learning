from fundamentals_library.computations import *
from constants import *

def num_modifier(num: int, desired_digits: int) -> str:

    num_of_digits: int = 1
    test_num: int = num

    while test_num > TWO_DIGIT_NUM_MIN:

        test_num /= TWO_DIGIT_NUM_MIN
        num_of_digits += 1

    return str(num).zfill(difference(desired_digits, num_of_digits))