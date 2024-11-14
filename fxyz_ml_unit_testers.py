from fxyz_ml_math_alg import *
from fxyz_ml_consts import *

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
    
    if num_of_terms < 1 or int(num_of_terms) == False or common_ratio == zero_base:

        return None

    geo_seq_arr: float = [first_term]
    current_rank = 2

    while current_rank < num_of_terms:

        geo_seq_arr.append(nth_term_arith(first_term, current_rank, common_ratio))
        current_rank += 1

    return geo_seq_arr