from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *
from math_library.number_theory import *
from math_library.differential_calculus import *
import math


# Needs Validation
def get_tax_status_ind(status: str) -> int:

    if status == "single": return 0
    if status == "married_jt": return 1
    if status == "married_fs": return 2
    if status == "head_of_household": return 3

    return -1

# Comment this section through and make sure the double indices work.
def expected_federal_tax(income: int, year: int, status: str) -> int:

    if not isinstance(income, (float, int, list)): return None
    
    if not isinstance(year, int): 
        
        try:

            year = int(year)

        except ValueError:
        
            return None

    
    total_income = SUM_INIT

    if isinstance(income, list):

        INCOME_LEN: int = len(income)

        if not validate_numeric_list(income, INCOME_LEN): return None

        for source in range(INCOME_LEN):

            total_income += income[source]

    else:

        total_income = income

    status_ind = get_tax_status_ind(status)

    total_income -= ST_TAX_DED[status_ind]

    # Calculate further deductions below.

    deductions: int = SUM_INIT

    # Calculations (Refer to 2.2 in the Alg Book for method)

    taxable_income: int = difference(total_income, deductions)

    tr_ind: int = FIRST_IND
    taxable_amount: float = product(FED_TR_PERC[tr_ind], FED_TR_AMT[tr_ind][status_ind])

    fed_tax: float = product(FED_TR_PERC[tr_ind], taxable_amount)

    taxable_income -= taxable_amount
    tr_ind += 1
    previous_taxable_amount: float = taxable_amount

    while taxable_income > 0 or tr_ind < subtract_one(len(FED_TR_PERC)):

        prev_tr_ind = subtract_one(tr_ind)

        previous_threshold: int = FED_TR_AMT[prev_tr_ind][status_ind]
        tax_rate: float = FED_TR_PERC[tr_ind]
        taxable_amount = difference(taxable_income, previous_threshold)

        fed_tax += add(previous_taxable_amount, product(tax_rate, taxable_amount))
        previous_taxable_amount = product(FED_TR_PERC[tr_ind], FED_TR_AMT[tr_ind][status_ind])

        taxable_income -= taxable_amount
        tr_ind += 1

    return fed_tax


    