from math_library.fund_comp import *
from fundamentals_library.constants import *
from unit_testers import *
"""
test_arith_seq_arr = build_arithmethic_sequence(-293, 10/3, 75)
test_geo_seq_arr = build_geometric_sequence(2, 1/3, 0)

print("Arithmetic:", test_arith_seq_arr, "\n\nGeometric:", test_geo_seq_arr)
"""

# g_to_v_unit_tester()

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

test_mult_then_divide(8)