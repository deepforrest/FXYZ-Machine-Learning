from fundamentals_library.computations import *
from fundamentals_library.unit_conversions import *
import math

# Part 1: Readibility Constants
AC_DISC_COEFF: int = 4
BINARY_BASE: int = 2
DENOM_INDEX: int = 1
CENTER_HOR_VAL: int = 0
CENTER_VERT_VAL: int = 0
DISC_THRESH: int = 0
FIRST_IND: int = 0
FRACT_ARR_LEN: int = 2
HOR_DIR: str = "horizontal"
INF_CRE: float = 0.000_001
LAST_IND: int = -1
LEN_BINOMIAL_COEFFS: int = 2
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
RIGHT_ANGLE: int = 90
SCALAR_LEN: int = 1
SCI_BASE: int = 10
SUM_INIT: int = 0
VARIANCE_THRESHOLD: int = 30
WHOLE_NUM_MIN: int = 0   #for functions that require whole numbers
NATURAL_NUM_MIN: int = 1
VER_DIR: str = "vertical"
ZERO_ANGLE: int = 0
ZERO_BASE: int = 0
ZERO_COEFF: int = 0
ZERO_DENOM: int = 0
ZERO_LEN: int = 0
ZERO_MASS: int = 0
ZEROTH_POWER: int = 0

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

# Part 2: Science Constants

# Constants to make as a function of units:

#1 - Speed of Light (length_unit, time_unit)
#2 - Gravitational Acceleration Constant (length_unit, time_unit)
#3 - Gravitational Force Constant (length_unit, time_unit, mass_unit)
#4 - Electrostatic Force Constant (length_unit, time_unit, charge_unit)