from fundamentals_library.computations import *
from fundamentals_library.unit_conversions import *

# Part 1: Readibility Constants
BINARY_BASE: int = 2
DENOM_INDEX: int = 1
DISC_THRESH: int = 0
HOR_DIR: str = "horizontal"
INF_CRE: float = 0.000_1
NUM_DIGITS_INIT: int = 1
NUM_INDEX: int = 0
PRODUCT_INIT: int = 1
SCI_BASE: int = 10
SUM_INIT: int = 0
VARIANCE_THRESHOLD: int = 30
WHOLE_NUM_MIN: int = 0   #for functions that require whole numbers
NATURAL_NUM_MIN: int = 1
VER_DIR: str = "vertical"
ZERO_BASE: int = 0
ZERO_DENOM: int = 0
ZEROTH_POWER: int = 0

FULL_CIRCLE_DEG: float = 360
FULL_CIRCLE_GRAD: float = 400
FULL_CIRCLE_RAD: float = 2 * math.pi

SINGLE_DIGIT_NUM_MIN: int = 9
TWO_DIGIT_NUM_MIN: int = 10
TWO_DIGIT_NUM_MAX: int = 99
THREE_DIGIT_NUM_MIN: int = 100
THREE_DIGIT_NUM_MAX: int = 999

# For arrays with ordered nums for points
X_IND, Y_IND, Z_IND = 0, 1, 2

# Part 2: Science Constants

# Constants to make as a function of units:

#1 - Speed of Light (length_unit, time_unit)
#2 - Gravitational Acceleration Constant (length_unit, time_unit)
#3 - Gravitational Force Constant (length_unit, time_unit, mass_unit)
#4 - Electrostatic Force Constant (length_unit, time_unit, charge_unit)