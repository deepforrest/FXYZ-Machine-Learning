from fundamentals_library.computations import *
from fundamentals_library.unit_conversions import *
import math

# Part 1: Readibility Constants
AC_DISC_COEFF: int = 4
ALG_ARR_LEN: int = 4
BINARY_BASE: int = 2
DENOM_INDEX: int = 1
CENTER_HOR_VAL: int = 0
CENTER_VERT_VAL: int = 0
CHECK_INPUTS: str = "Please check your inputs and try again."
DISC_THRESH: int = 0
EMPTY_LIST: list = []
FIRST_IND: int = 0
FRACT_ARR_LEN: int = 2
HOR_DIR: str = "horizontal"
INF_CRE: float = 1 ** -6
LAST_IND: int = -1
LEN_BINOMIAL_COEFFS: int = 2
LIST_OF_LISTS_LEN: int = 1
MIN_RANKS: int = 2
NEXT_IND: int = 1
NO_REMAINDER: int = 0
NUM_DIGITS_INIT: int = 1
NUM_SIDES_TRI: int = 3
NUM_SIDES_QUAD: int = 4
NUM_INDEX: int = 0
POINT_LEN_2D: int = 2
POINT_LEN_3D: int = 3
PRODUCT_INIT: int = 1
QUAD_COEFF_LEN: int = 3
RIGHT_ANGLE: int = 90
SCALAR_LEN: int = 1
SCI_BASE: int = 10
SUM_INIT: int = 0
VARIANCE_THRESHOLD: int = 30
WHOLE_NUM_MIN: int = 0   #for functions that require whole numbers
NATURAL_NUM_MIN: int = 1
UNIT_BASE: int = 1
UNIT_COEFF: int = 1
VER_DIR: str = "vertical"
ZERO_ANGLE: int = 0
ZERO_BASE: int = 0
ZERO_COEFF: int = 0
ZERO_DENOM: int = 0
ZERO_LEN: int = 0
ZERO_MASS: int = 0
ZEROTH_POWER: int = 0

QUAD_LEAD_COEFF_IND: int = 0
QUAD_LIN_COEFF_IND: int = 1
QUAD_CONST_COEFF_IND: int = 2

FULL_CIRCLE_DEG: float = 360
FULL_CIRCLE_GRAD: float = 400
FULL_CIRCLE_RAD: float = 2 * math.pi

ONE_DIGIT_NUM_MAX: int = 9
TWO_DIGIT_NUM_MIN: int = 10
TWO_DIGIT_NUM_MAX: int = 99
THREE_DIGIT_NUM_MIN: int = 100
THREE_DIGIT_NUM_MAX: int = 999

SEC_PER_MIN: int = 60
MIN_PER_HR: int = 60
HR_PER_DAY: int = 24
MONTH_PER_YEAR: int = 12
DAY_PER_WEEK: int = 7
DAY_PER_YEAR: int = 365.24

# For arrays with ordered nums for points
X_IND, Y_IND, Z_IND = 0, 1, 2

A_IND: int = 0
B_IND: int = 1
H_IND: int = 2
K_IND: int = 3
# Part 1: Business Constants
# https://www.fidelity.com/learning-center/personal-finance/tax-brackets
SF_IND: int = 0
MFJ_IND: int = 1
MFS_IND: int = 2
HOH_IND: int = 3

# These can probably be stored in a different area and called more appropriately...
FTR_10_nHOH: int = 11_600
FTR_10_HOH: int = 16_550

FTR_12_nHOH: int = 47_150
FTR_12_HOH: int = 63_100

FTR_22_nHOH: int = 100_525
FTR_22_HOH: int = 100_500

FTR_24_nHOH: int = 191_950
FTR_24_HOH: int = 191_950

FTR_32_nHOH: int = 243_725
FTR_32_HOH: int = 243_700

FTR_35_nHOH: int = 11_600
FTR_35_HOH: int = 609_350

ST_TAX_DED_nHOH: int = 14_600
ST_TAX_DED_HOH: int = 21_900

# 2024, Max Amts            Single,        Mar. Jt,          Mar. Sep,      HoH
FED_TR_10: tuple[int] = (FTR_10_nHOH, double(FTR_10_nHOH), FTR_10_nHOH, FTR_10_HOH)
FED_TR_12: tuple[int] = (FTR_12_nHOH, double(FTR_12_nHOH), FTR_12_nHOH, FTR_12_HOH)
FED_TR_22: tuple[int] = (FTR_22_nHOH, double(FTR_22_nHOH), FTR_22_nHOH, FTR_22_HOH)
FED_TR_24: tuple[int] = (FTR_24_nHOH, double(FTR_24_nHOH), FTR_24_nHOH, FTR_24_HOH)
FED_TR_32: tuple[int] = (FTR_32_nHOH, double(FTR_32_nHOH), FTR_32_nHOH, FTR_32_HOH)
FED_TR_35: tuple[int] = (FTR_35_nHOH, double(FTR_35_nHOH), FTR_35_nHOH, FTR_35_HOH)
# Anything above the thresholds @ 35 is at 37%
FED_TR_AMT: tuple[int] = (FED_TR_10, FED_TR_12, FED_TR_22, FED_TR_24, FED_TR_32, FED_TR_35)

ST_TAX_DED: tuple[int] = (ST_TAX_DED_nHOH, double(ST_TAX_DED_nHOH), ST_TAX_DED_nHOH, ST_TAX_DED_HOH)
FED_TR_PERC: tuple[int] = (0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37)



# Part 2: Science Constants


# Constants to make as a function of units:

#1 - Speed of Light (length_unit, time_unit)
#2 - Gravitational Acceleration Constant (length_unit, time_unit)
#3 - Gravitational Force Constant (length_unit, time_unit, mass_unit)
#4 - Electrostatic Force Constant (length_unit, time_unit, charge_unit)