from fundamentals_library.computations import *
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

def factors(num: int) -> list:

    factors_arr = [1] # one is always a factor
    
    starting_factor: int = 1
    
    mid_point = half(num) # Ensures half the work is done, since n/2 + k is never a factor of n where k > 0

    while starting_factor <= mid_point:

        if remainder(num, starting_factor) == 0:

            factors_arr.append(starting_factor)

        starting_factor += 1

    return factor_arr
