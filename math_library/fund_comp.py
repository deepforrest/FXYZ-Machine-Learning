from fundamentals_library.constants import *

# Function 01 Family: Elementary Functions
# These functions were created to remove the clutter of +, -, *, and / operations to make them more readable and intentional.  This also prevents mismatched parentheses in most cases.
# Current number of functions: 9

# Function 01-001
def add(first_num: float, second_num: float) -> float:

    return first_num + second_num


# Function 01-002
def difference(first_num: float, second_num: float) -> float:

    return first_num - second_num


# Function 01-003
def product(first_num: float, second_num: float) -> float:

    return first_num * second_num


# Function 01-004
# This function will likely need to be updated to handle indeterminant forms.
def float_quotient(num: float, denom: float) -> float:

    return num / denom if denom != ZERO_DENOM else None


# Function 01-005
# This function will likely need to be updated to handle indeterminant forms.
def int_quotient(num: float, denom: float) -> int:

    # // means integer division
    return num // denom if denom != ZERO_DENOM else None


# Function 01-006
# This function may need more checks to ensure the wrong data type is not passed.
def remainder(num: float, denom: float) -> int:

    return num % denom if denom != ZERO_DENOM else None


# Function 01-007
def exponentiate(base: float, power: float) -> float:

    if base != ZERO_BASE:

        if power!= ZEROTH_POWER:
        
            return base ** power
        
        return ZERO_BASE
    
    return None

#Function 01-008
def root(base: float, nth_root: float) -> float:

    # Calls Functions 01-007, ######, & 
    return exponentiate(base, reciprocal(nth_root))

def sci_note(power: int) -> float:

    return exponentiate(SCI_BASE, power)

# Part II: Advanced Math Functions, Nonarray

def neg(num: float) -> float:

    return -num


def reciprocal(num: float) -> float:

    return float_quotient(1, num) if num != ZERO_DENOM else None


def abs_value(num: float) -> float:

    return num if num >= WHOLE_NUM_MIN else neg(num)


def add_one(num):

    return add(num, 1)


def subtract_one(num):

    return difference(num, 1)


def polynomial(coeff: float, base: float, power: float) -> float:

    return product(coeff, exponentiate(base, power))


def num_midpoint(first_num: float, second_num: float) -> float:

    return float_quotient(add(first_num, second_num), 2)


def factorial(num: int) -> int:

    if num >= WHOLE_NUM_MIN and int(num) == True:

        result = PRODUCT_INIT
        counter = num

        while counter > NATURAL_NUM_MIN:

            result *= counter
            counter -= 1

        return result

    return None


def product_op(num_start: int, num_finish: int) -> int:

    # Validates that numbers are starting from low to high, switches them if needed.
    input_start = num_start if num_start <= num_finish else num_finish
    input_finish = num_finish if num_finish >= num_start else num_start
    
    return float_quotient(factorial(input_finish), factorial(input_start))