from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *

def calc_data_avg(data_arr: float) -> float:

    sum = SUM_INIT
    count = 0

    for pt in range(len(data_arr)):

        sum += data_arr[pt]
        count += 1
    
    return float_quotient(sum, count)


def calc_data_variance(data_arr: float) -> float:

    data_avg = calc_data_avg(data_arr)

    sum_squares: float = SUM_INIT

    count = 1 if difference(range(len(data_arr)), 1) >= VARIANCE_THRESHOLD else 0

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

