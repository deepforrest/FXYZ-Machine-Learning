from fxyz_ml_consts import *

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

    return num if num >= WHOLE_NUM_MIN else -num


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


def polynomial_derivative(coeff: float, base: float, power: float) -> float:

    # Checks for instances of divide by 0 and/or indeterminant forms
    if power <= ZEROTH_POWER and base == ZERO_BASE:
        
        return None

    return polynomial(product(coeff, power), base, subtract_one(power))


def product_op(num_start: int, num_finish: int) -> int:

    # Validates that numbers are starting from low to high, switches them if needed.
    input_start = num_start if num_start <= num_finish else num_finish
    input_finish = num_finish if num_finish >= num_start else num_start
    
    return float_quotient(factorial(input_finish), factorial(input_start))


# Part III: Algebra I Calculations

def slope_from_two_points(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Prevents divide by zero returns
    if x_2 == x_1: return None

    return(float_quotient(difference(y_2, y_1), difference(x_2, x_1)))


# Ready To Test
def slope_from_point_array(point_arr_2: float, point_arr_1: float) -> float:

    # Validates arrays to ensure they have two coordinates:
    if len(point_arr_2) != 2 and len(point_arr_1) != 2:

        return None

    for coordinate in range(len(point_arr_2)):

        if float(point_arr_2[coordinate]) == False or float(point_arr_1[coordinate]) == False:

            return None

    return(float_quotient(difference(point_arr_2[1], point_arr_2[0]), difference(point_arr_1[1], point_arr_1[0])))


def perp_slope(slope: float) -> float:

    return neg(reciprocal(slope)) if slope != ZERO_DENOM else None


def normal_slope(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    if y_2 == y_1:

        return None
    
    return neg(float_quotient(difference(x_2, x_1), difference(y_2, y_1)))

# Needs to be thought out
#def slope_at_point(poly_coeff_arr: List[float]):
#
#   return -1


def midpoint_2d_arr(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    # Returns as a 2d ordered pair
    return [num_midpoint(x_2, x_1), num_midpoint(y_2, y_1)]


def distance_2d(y_2: float, y_1: float, x_2: float, x_1: float) -> float:

    return root(add(exponentiate(difference(x_1, x_2), 2), (exponentiate(difference(y_1, y_2), 2))), 2)


def general_to_vertex_quad(lead_coeff: float, linear_coeff: float, const: float) -> float:

    if lead_coeff == 0:
        
        print("Not a quadratic function when a = 0")
        return None

    calc_array = [lead_coeff, linear_coeff, const]
    horizontal_offset = float_quotient(neg(linear_coeff), product(2, lead_coeff))
    power = 2
    vertical_offset = 0

    
    while power >= ZEROTH_POWER:
    
        for num in range(len(calc_array)):
        
            # Debugger Line
            # print("k = ", k, "+ ", calc_array[num], " * ", h, "^", power)
            
            vertical_offset += polynomial(calc_array[num], horizontal_offset, power)
            power -= 1

    # Printing conditions for cleaner output
    
    horizontal_sign = "-" if horizontal_offset >= whole_num_min else "+"
    vertical_sign = "+" if vertical_offset >= whole_num_min else "-"
    print_hor_offset: str = str(horizontal_offset) if horizontal_offset >= whole_num_min else abs_value(horizontal_offset)
    print_vert_offset: str = str(vertical_offset) if vertical_offset >= whole_num_min else abs_value(vertical_offset)
    print_lead_coeff: str = str(lead_coeff) if lead_coeff != 1 else ""
    
    print("y = ", print_lead_coeff, "(x", horizontal_sign, print_hor_offset, ") ^ 2", vertical_sign, print_vert_offset)
    
    return [horizontal_offset, vertical_offset]

# Discrete Math Terms

def nth_term_arith(first_term: float, nth_rank: int, common_diff: float) -> float:

    return add(first_term, product(subtract_one(nth_rank), common_diff))


def nth_term_geo(first_term: float, nth_rank: int, common_ratio) -> float:

    return polynomial(first_term, common_ratio, subtract_one(nth_rank))


def find_comm_diff(first_term: float, nth_term: float, nth_rank: int) -> float:

    if int(nth_rank) == False or nth_rank < 2:

        return None

    return float_quotient(difference(nth_term, first_term), subtract_one(nth_rank))


def find_first_term_arith(nth_term: float, nth_rank: float, common_diff: float) -> float:

    return difference(nth_term, difference(nth_rank, 1))


def arith_sum(num_terms: int, first_term: float, last_term: float) -> float:

    return float_quotient(product(num_terms, add(first_term, last_term)), 2)

def geo_sum_part(num_terms: float, nth_term: int, common_ratio: float) -> float:

    return float_quotient(difference(1, exponentiate(common_ratio, nth_term)), difference(1, common_ratio))

def geo_sum_inf(common_ratio: float, first_term: float) -> float:

    # Note that the common_ratio must be between -1 and +1, exclusive.
    return float_quotient(first_term, difference(1, common_ratio)) if abs_value(common_ratio) < 1 else None


# Statistics
def calc_data_avg(data_arr: float) -> float:

    sum = SUM_INIT
    count = 0

    for pt in range(len(data_arr)):

        sum += data_arr[pt]
        count += 1
    
    return float_quotient(sum, count)


def calc_data_variance(data_arr: float) -> float:

    data_avg = calc_data_avg(data_arr)

    sum_squares: float = 0

    count = 1 if difference(range(len(data_arr)), 1) >= variance_threshold else 0

    for pt in range(len(data_arr)):

        sum_squares += exponentiate(difference(data_arr[pt], data_avg), 2)
        count += 1

    return(float_quotient(sum_squares, count))


def calc_data_stdev(data_arr: float) -> float:

    return root(calc_data_variance(data_arr), 2)


def find_data_median(data_arr: float) -> float:

    data_arr.sort()
    mid_index = int_quotient(range(len(data_arr)) - 1, 2)

    return data_arr[mid_index] if remainder(mid_index, 2) == 0 else num_midpoint(data_arr[mid_index - 1], data_arr[mid_index])

def find_data_mode(data_arr: float) -> float:

    # What needs to be done:
    # 1 - Sort the input array and create two arrays.
    # 2 – Populate the num array with only a single copy of a number
    # 3 – Populate the counter array by scanning the full array and comparing to the number array
    
    data_arr.sort()
    num_arr = []
    count_arr = []

    # What is this for?
    for i in range(len(data_arr)):

        num_arr.append()

    # And this?
    for i in range(len(num_arr)):

        count_arr.append(1)

    # Rework algorithm to be less complex:
    for i in range(len(num_arr)):

        for j in range(len(data_arr)):

            if data_arr[j] == num_arr[i]: count_arr[i] +=1

    # Check to see if there are duplicate modes


# Part X: Test Functions

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

# TESTS

test_num: int = 12
test_arr: float = [-1, -4, +4]
#print(mult_then_divide(test_num))
#print(test_num, "! = ", f"{factorial(test_num):,}")

# general_to_vertex_quad(test_arr[0], test_arr[1], test_arr[2])

def g_to_v_unit_tester():

    distance = 30

    start_a = -10
    stop_a = start_a + distance
    test_a = start_a
    
    start_b = -10
    stop_b = start_b + distance
    test_b = start_b

    start_c = -10
    stop_c = start_c + distance
    test_c = start_c

    num_iter = 0

    while test_a <= stop_a:

        test_b = start_b
        test_c = start_c
        
        while test_b <= stop_b:

            test_c = start_c

            while test_c <= stop_c:

                print("When a = ", test_a, ", b = ", test_b, ", and c = ", test_c)
                general_to_vertex_quad(test_a, test_b, test_c)
                print("\n\n")
                test_c += 1
                num_iter += 1

            test_b += 1

        test_a += 1

    print("Number of iterations = ", f"{num_iter:,}")

# g_to_v_unit_tester()