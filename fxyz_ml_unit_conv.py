from fxyz_ml_math_ops import *

# Prefixes
TERA_PREFIX: str = "T"
GIGA_PREFIX: str = "G"
MEGA_PREFIX: str = "M"
KILO_PREFIX: str = "k"
CENTI_PREFIX: str = "c"
MILLI_PREFIX: str = "m"
MICRO_PREFIX: str = "µ"
NANO_PREFIX: str = "n"
NO_PREFIX: str = ""

# Energy Conversions
JOULE_UNIT: str = "J"
CAL_UNIT: str = "cal"
LITER_X_ATM: str = "L*atm"
CUBIC_FT_PSI = "ft^3*psi"

JOULE_TO_CAL: float = 4.184
JOULE_TO_LITER_X_ATM: float = 101.325
JOULE_TO_CUBIC_FT_PSI: float = 6894.76
SELF: float = 1

# Pressure Conversions
PA_UNIT: str = "Pa"
ATM_UNIT: str = "atm"
BAR_UNIT: str = "bar"

PA_TO_ATM: float = reciprical(101325)
PA_TO_BAR: float = reciprical(exponentiate(10, 5))

ENERGY_CONVERSIONS: float = {

    JOULE_UNIT: {

        JOULE_UNIT: SELF,
        CAL_UNIT: JOULE_TO_CAL,
        LITER_X_ATM: JOULE_TO_LITER_X_ATM,
        CUBIC_FT_PSI: JOULE_TO_CUBIC_FT_PSI

    },

    CAL_UNIT: {

        JOULE_UNIT: reciprical(JOULE_TO_CAL),
        CAL_UNIT: SELF,
        LITER_X_ATM: float_quotient(JOULE_TO_CAL, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI: float_quotient(JOULE_TO_CAL, JOULE_TO_CUBIC_FT_PSI)

    },

    LITER_X_ATM: {

        JOULE_UNIT: reciprical(JOULE_TO_LITER_X_ATM),
        CAL_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_CAL),
        LITER_X_ATM: SELF,
        CUBIC_FT_PSI: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_CUBIC_FT_PSI),

    },

    CUBIC_FT_PSI: {

        JOULE_UNIT: reciprical(JOULE_TO_CUBIC_FT_PSI),
        CAL_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_CAL),
        LITER_X_ATM: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI: SELF


    }

}

PRESSURE_CONVERSIONS: float = {}