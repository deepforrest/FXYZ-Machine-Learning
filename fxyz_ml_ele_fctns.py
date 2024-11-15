from fxyz_ml_math_ops import *

def reduce_fraction(num: int, denom: int) -> int:

    # Function Steps:
    #! Determine all factors of numerator and denomonator
    #! Go through both arrays and cancel out factors
    # Multiply remaining factors together
    # Return an array with reduce numerator and denominator

    # Stage 1: Get Factors
    num_to_reduce: int = num
    denom_to_reduce: int = denom

    num_factors = []
    denom_factors = []

    # Stage 2: ???

    # Stage 3: Create Reduced Numbers
    reduced_num = PROD_INIT
    reduced_denom = PROD_INIT

    if range(len(num_factors)) == range(len(denom_factors)):

        for i in num_factors:

            reduced_num *= num_factors[i]
            reduced_denom *= denom_factors[i]

        return [reduced_num, reduced_denom]

    else: 

        for i in num_factors:

            reduced_num *= num_factors[i]

        for i in denom_factors:

            reduced_denom *= denom_factors[i]

        return [reduced_num, reduced_denom]