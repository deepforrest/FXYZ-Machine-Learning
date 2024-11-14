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

#Self Conversion Definition
SELF: float = 1

# Energy Conversions
JOULE_UNIT: str = "J"
CAL_UNIT: str = "cal"
LITER_X_ATM_UNIT: str = "L*atm"
CUBIC_FT_PSI_UNIT = "ft^3*psi"
WATT_HR_UNIT = "W*hr"

JOULE_TO_CAL: float = 4.184
JOULE_TO_LITER_X_ATM: float = 101.325
JOULE_TO_CUBIC_FT_PSI: float = 6894.76
JOULE_TO_WATT_HR: float = 3600

# Pressure Conversions
PA_UNIT: str = "Pa"
ATM_UNIT: str = "atm"
BAR_UNIT: str = "bar"
TORR_UNIT: str = "torr"

PA_TO_ATM: float = reciprical(101325)
PA_TO_BAR: float = reciprical(exponentiate(10, 5))
PA_TO_TORR: float = reciprical(133.322)
PA_TO_PSI: float = reciprical(6894.76)

ENERGY_CONVERSIONS: float = {

    JOULE_UNIT: {

        JOULE_UNIT: SELF,
        CAL_UNIT: JOULE_TO_CAL,
        LITER_X_ATM_UNIT: JOULE_TO_LITER_X_ATM,
        CUBIC_FT_PSI_UNIT: JOULE_TO_CUBIC_FT_PSI,
        WATT_HR_UNIT: JOULE_TO_WATT_HR,

    },

    CAL_UNIT: {

        JOULE_UNIT: reciprical(JOULE_TO_CAL),
        CAL_UNIT: SELF,
        LITER_X_ATM_UNIT: float_quotient(JOULE_TO_CAL, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI_UNIT: float_quotient(JOULE_TO_CAL, JOULE_TO_CUBIC_FT_PSI),
        WATT_HR_UNIT: float_quotient(JOULE_TO_CAL, JOULE_TO_WATT_HR),

    },

    LITER_X_ATM_UNIT: {

        JOULE_UNIT: reciprical(JOULE_TO_LITER_X_ATM),
        CAL_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_CAL),
        LITER_X_ATM_UNIT: SELF,
        CUBIC_FT_PSI_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_CUBIC_FT_PSI),
        WATT_HR_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_WATT_HR),

    },

    CUBIC_FT_PSI_UNIT: {

        JOULE_UNIT: reciprical(JOULE_TO_CUBIC_FT_PSI),
        CAL_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_CAL),
        LITER_X_ATM_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI_UNIT: SELF,
        WATT_HR_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_WATT_HR),


    },

    WATT_HR_UNIT: {

        JOULE_UNIT: reciprical(JOULE_TO_WATT_HR),
        CAL_UNIT: float_quotient(JOULE_TO_WATT_HR, JOULE_TO_CAL),
        LITER_X_ATM_UNIT: float_quotient(JOULE_TO_WATT_HR, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI_UNIT: float_quotient(JOULE_TO_WATT_HR, JOULE_TO_CUBIC_FT_PSI),
        WATT_HR_UNIT: SELF,

    }

}

PRESSURE_CONVERSION: float = {

    PA_UNIT: {

        PA_UNIT: SELF,
        ATM_UNIT: PA_TO_ATM,
        BAR_UNIT: PA_TO_BAR,
        TORR_UNIT: PA_TO_TORR,

    },
    
    ATM_UNIT: {

        PA_UNIT: reciprical(PA_TO_ATM),
        ATM_UNIT: SELF,
        BAR_UNIT: float_quotient(PA_TO_ATM, PA_TO_BAR),
        TORR_UNIT: float_quotient(PA_TO_ATM, PA_TO_TORR),

    },

    BAR_UNIT: {

        PA_UNIT: reciprical(PA_TO_BAR),
        ATM_UNIT: float_quotient(PA_TO_BAR, PA_TO_ATM),
        BAR_UNIT: SELF,
        TORR_UNIT: float_quotient(PA_TO_BAR, PA_TO_TORR),
    },

    TORR_UNIT: {
        
        PA_UNIT: reciprical(PA_TO_TORR),
        ATM_UNIT: float_quotient(PA_TO_TORR, PA_TO_ATM),
        BAR_UNIT: float_quotient(PA_TO_TORR, PA_TO_BAR),
        TORR_UNIT: SELF,
    }


}