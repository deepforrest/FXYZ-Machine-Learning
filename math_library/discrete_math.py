from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *

# Discrete Math Terms

def nth_term_arith(first_term: float, nth_rank: int, common_diff: float) -> float:

    return add(first_term, product(subtract_one(nth_rank), common_diff))


def nth_term_geo(first_term: float, nth_rank: int, common_ratio) -> float:

    return polynomial(first_term, common_ratio, subtract_one(nth_rank))


def find_comm_diff(first_term: float, nth_term: float, nth_rank: int) -> float:

    if not int(nth_rank) or nth_rank < MIN_RANKS:

        return None

    return float_quotient(difference(nth_term, first_term), subtract_one(nth_rank))


def find_first_term_arith(nth_term: float, nth_rank: float, common_diff: float) -> float:

    return difference(nth_term, subtract_one(nth_rank))


def arith_sum(num_terms: int, first_term: float, last_term: float) -> float:

    return half(product(num_terms, add(first_term, last_term)))


def geo_sum_part(num_terms: float, nth_term: int, common_ratio: float) -> float:

    numerator: float = diff_from_one(exponentiate(common_ratio, nth_term))

    denominator: float = diff_from_one(common_ratio)

    return float_quotient(numerator, denominator)


def geo_sum_inf(common_ratio: float, first_term: float) -> float:

    # Note that the common_ratio must be between -1 and +1, exclusive.
    if abs_value(common_ratio) < 1:

        return f'Sum diverges since |{common_ratio}| < 1'
        
    return float_quotient(first_term, diff_from_one(common_ratio))