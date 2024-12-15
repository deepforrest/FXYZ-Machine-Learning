from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *

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

    for digit in range(len(digit_arr)):

        num_prod *= digit_arr[digit]

    # Return Product
    return num_prod

# Function 04: Splt Numbers Into An Array
# Splits a number into its components as an array.
# Example: 2491 -> [2000, 400, 90, 1]
def split_num_into_arr(num: int) -> list:

    num_arr = []
    num_of_digits: int = len(str(num))

    for digit in range(len(num)):

        num_arr.append[product(digit, sci_note(num_of_digits))]
        num_of_digits -= 1

    return num_arr

# Function 05: Digit Product To Sum Ratio
# Returns a float to denote whether the product or sum is greater
# Domain > 0
def prod_to_sum_digits_ratio(num: int) -> float:

    return float_quotient(prod_of_nz_digits(num), sum_of_digits(num))

def mult_then_divide(num_times: int):

    counter: int = 1
    numerator: int = 1
    denominator: int = 1

    while counter <= num_times:
        
        if divisible_by_n(counter, 2) == True:
        
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

    factors_arr: list = [1] # One is always a factor
    starting_factor: int = 2
    
    # Ensures half the work is done, since n/2 + k is never a factor of n where k > 0
    mid_point: float = half(num) 

    while starting_factor <= mid_point:

        if remainder(num, starting_factor) == 0:

            factors_arr.append(starting_factor)

        starting_factor += 1

    return factors_arr

def num_of_doublings(start_num: float, final_num: float) -> int:

    # Validation 1: Checks for zeros in either entry.
    if start_num == WHOLE_NUM_MIN or final_num == WHOLE_NUM_MIN:

        print(f'Zero cannot be doubled')
        return -1

    # Validation 2: Ensures numbers are signless.
    num_to_analyze: float = start_num if start_num > WHOLE_NUM_MIN else abs_value(start_num)
    num_to_finish: float = final_num if final_num > WHOLE_NUM_MIN else abs_value(final_num)

    # Validation 3: Swaps numbers if entered out of order.
    if num_to_analyze > num_to_finish:

        num_to_analyze, num_to_finish = num_to_finish, num_to_analyze

    # Now the analysis
    doubling_count: int = SUM_INIT

    while num_to_analyze < num_to_finish:

        num_to_analyze = double(num_to_analyze)
        doubling_count += 1

    return doubling_count

def rebase_number(num: int, current_base: int, new_base: int) -> int:

    # Validation
    validation_arr = [num, current_base, new_base]
    num_converted: bool = False

    for entry in range(len(validation_arr)):

        if not isinstance(validation_arr[entry], int):

            num_converted = True

            try:

                validation_arr[entry] = int(validation_arr[entry])

            except ValueError:

                print(f'The function rebase_number: {validation_arr[entry]} at index {entry} is not valid 
                      in the validation_array [num, current_base, new_base].  {CHECK_INPUTS}')
                
                return None
    
    # Updates entries if conversion happened:
    if num_converted:

        num = validation_arr[0]
        current_base = validation_arr[1]
        new_base = validation_arr[2]

    # Calculation
    new_num: int = SUM_INIT
    binary_arr: list[int] = EMPTY_LIST
    power: int = 1
    test_base: int = new_base

    # Generate a new array of 1s and 0s to represent the base to that power
    while exponentiate(test_base, power) < num:

        binary_arr.append(1)
        power += 1

    # Create new number from binary arr
    return EMPTY_LIST

def binomial_coeff(kth_term: int, nth_exponent) -> int:

    # Switches the numbers if entered out order
    if nth_exponent > kth_term:

        nth_exponent, kth_term = kth_term, nth_exponent

    numerator:int = factorial(nth_exponent)
    denominator: int = product(factorial(kth_term), factorial(difference(nth_exponent, kth_term)))

    return float_quotient(numerator, denominator)