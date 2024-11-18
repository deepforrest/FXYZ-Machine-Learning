from MATH_FUN.fund_comp import *
from fundamentals_library.constants import *

def divisible_by_n(num: int, divisor: int) -> bool:

    return True if remainder(num, divisor) == 0 else False


# Function 02: Sum of Digits
# Returns the sum of all digits in an integer
def sum_of_digits(num: int) -> int:
    
    # Shortcut using mapping techniques
    return sum(map(int, str(abs.value(num))))

# Function 03: Product of Non-Zero Digits
# Takes a number and takes the product of all nonzero digits:
# Example: 42041 -> [4, 2, 4, 1] -> 32
def prod_of_nz_digits(num: int) -> int:

    num_prod: int = PRODUCT_INIT
    digit_arr: int = []
    num_to_parse: int = abs_value(num)

    # Step Two: Parse Number & Discard All Zero Digits

    for digit in range(len(num_to_parse)):

        if digit > 0: digit_arr.append[digit]

    # Return Product
    return product(digit_arr)

# Function 04: Splt Numbers Into An Array
# Splits a number into its components.
# Example: 2491 -> [2000, 400, 90, 1]
def split_num_into_arr(num: int) -> int:

    num_arr = []
    num_of_digits: int = len(str(num))

    for digit in range(len(num)):

        num_arr.append[exponentiate(digit, num_of_digits)]
        num_of_digits -= 1

    return num_arr

# Function 05: Digit Product To Sum Ratio
# Returns a float to denote whether the product or sum is greater
# Domain > 0
def prod_to_sum_digits_ratio(num: int) -> float:

    return(float_quotient(prod_of_nz_digits(num), sum_of_digits(num)))