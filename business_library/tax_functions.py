from fundamentals_library.computations import *
from fundamentals_library.constants import *
from fundamentals_library.validations import *
from math_library.number_theory import *
from math_library.differential_calculus import *
import math

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

    ind = get_status_ind(status) # Needs to be defined

    # Calculations (Refer to 2.2 in the Alg Book for method)
    total_income -= ST_DED_TAX[ind]

    tax_liability = SUM_INIT
    