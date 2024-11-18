from math_library.algebraic_functions import *
from math_library.differential_calculus import *
from math_library.discrete_math import *
from math_library.fund_comp import *
from math_library.number_theory import *
from math_library.statistics import *

from fundamentals_library.constants import *

def build_arithmethic_sequence(first_term: float, common_diff: float, num_of_terms: int) -> float:
    
    if num_of_terms < 1 or int(num_of_terms) == False:

        return None
    
    arith_seq_arr: float = [first_term]
    current_rank = 2

    while current_rank < num_of_terms:

        arith_seq_arr.append(nth_term_arith(first_term, current_rank, common_diff))
        current_rank += 1

    return arith_seq_arr


def build_geometric_sequence(first_term: float, common_ratio: float, num_of_terms: int) -> float:
    
    if num_of_terms < 1 or int(num_of_terms) == False or common_ratio == ZERO_BASE:

        return None

    geo_seq_arr: float = [first_term]
    current_rank = 2

    while current_rank < num_of_terms:

        geo_seq_arr.append(nth_term_arith(first_term, current_rank, common_ratio))
        current_rank += 1

    return geo_seq_arr

def test_common_diff(input_arr) -> float:

    if range(len(input_arr)) == 1:

        return None

    test_diff: float = input_arr[1] - input_arr[0]
    index = 2

    while index < range(len(input_arr)):

        if input_arr[index] - input_arr[index-1] != test_diff: return None

        index +=1

    return test_diff

# This function could be prone to errors due to Python's rounding.  Thus, it should be build to use numerators and denominators of the ratios to see if their reductions are the same.
def test_common_ratio(input_arr) -> float:

    if range(len(input_arr)) == 1:

        return None

    test_ratio: float = input_arr[1] - input_arr[0]
    index = 2

    return None

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

def test_mult_then_divide(num: int) -> list:

    start_num: int = 1
    test_arr = []

    while start_num <= num:

        test_num = mult_then_divide(start_num)
        test_arr.append(test_num)
        print(f'{start_num} generates a result of {test_num}')
        start_num += 1

    final_product: int = PRODUCT_INIT

    for result in range(len(test_arr)):

        final_product *= test_arr[result]
    
    print(f'The product of all numbers is {final_product}.')