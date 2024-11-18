from math_library.fund_comp import *
from fundamentals_library.constants import *

#Self Conversion Definition
SELF: float = 1

# PART 1: PREFIXES
YOTTA_PREFIX: str = "Y"
ZETTA_PREFIX: str = "Z"
EXA_PREFIX: str = "E"
PETA_PREFIX: str = "P"
TERA_PREFIX: str = "T"
GIGA_PREFIX: str = "G"
MEGA_PREFIX: str = "M"
KILO_PREFIX: str = "k"
HECTO_PREFIX: str = "h"
DECA_PREFIX: str = "da"
NO_PREFIX: str = ""
DECI_PREFIX: str = "d"
CENTI_PREFIX: str = "c"
MILLI_PREFIX: str = "m"
MICRO_PREFIX: str = "µ"
NANO_PREFIX: str = "n"
PICO_PREFIX: str = "p"
FEMTO_PREFIX: str = "f"
ATTO_PREFIX: str = "a"
ZEPTO_PREFIX: str = "z"
YOCTO_PREFIX: str = "y"

YOTTA_VALUE: float = sci_note(24)
ZETTA_VALUE: float = sci_note(21)
EXA_VALUE: float = sci_note(18)
PETA_VALUE: float = sci_note(15)
TERA_VALUE: float = sci_note(12)
GIGA_VALUE: float = sci_note(9)
MEGA_VALUE: float = sci_note(6)
KILO_VALUE: float = sci_note(3)
HECTO_VALUE: float = sci_note(2)
DECA_VALUE: float = sci_note(1)
NO_VALUE: float = sci_note(0)
DECI_VALUE: float = sci_note(neg(1))
CENTI_VALUE: float = sci_note(neg(2))
MILLI_VALUE: float = sci_note(neg(3))
MICRO_VALUE: float = sci_note(neg(6))
NANO_VALUE: float = sci_note(neg(9))
PICO_VALUE: float = sci_note(neg(12))
FEMTO_VALUE: float = sci_note(neg(15))
ATTO_VALUE: float = sci_note(neg(18))
ZEPTO_VALUE: float = sci_note(neg(21))
YOCTO_VALUE: float = sci_note(neg(24))


PREFIX_IND, VALUE_IND = 0, 1

YOTTA_DATASET: tuple = (YOTTA_PREFIX, YOTTA_VALUE)
ZETTA_DATASET: tuple = (ZETTA_PREFIX, ZETTA_VALUE)
EXA_DATASET: tuple = (EXA_PREFIX, EXA_VALUE)
PETA_DATASET: tuple = (PETA_PREFIX, PETA_VALUE)
TERA_DATASET: tuple = (TERA_PREFIX, TERA_VALUE)
GIGA_DATASET: tuple = (GIGA_PREFIX, GIGA_VALUE)
MEGA_DATASET: tuple = (MEGA_PREFIX, MEGA_VALUE)
KILO_DATASET: tuple = (KILO_PREFIX, KILO_VALUE)
HECTO_DATASET: tuple = (HECTO_PREFIX, HECTO_VALUE)
DECA_DATASET: tuple = (DECA_PREFIX, DECA_VALUE)
NO_DATASET: tuple = (NO_PREFIX, NO_VALUE)
DECI_DATASET: tuple = (DECI_PREFIX, DECI_VALUE)
CENTI_DATASET: tuple = (CENTI_PREFIX, CENTI_VALUE)
MILLI_DATASET: tuple = (MILLI_PREFIX, MILLI_VALUE)
MICRO_DATASET: tuple = (MICRO_PREFIX, MICRO_VALUE)
NANO_DATASET: tuple = (NANO_PREFIX, NANO_VALUE)
PICO_DATASET: tuple = (PICO_PREFIX, PICO_VALUE)
FEMTO_DATASET: tuple = (FEMTO_PREFIX, FEMTO_VALUE)
ATTO_DATASET: tuple = (ATTO_PREFIX, ATTO_VALUE)
ZEPTO_DATASET: tuple = (ZEPTO_PREFIX, ZEPTO_VALUE)
YOCTO_DATASET: tuple = (YOCTO_PREFIX, YOCTO_VALUE)

PREFIX_CONVERSION: float = {

    YOTTA_PREFIX: {

        YOTTA_PREFIX: SELF,
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, YOTTA_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, YOTTA_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, YOTTA_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, YOTTA_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, YOTTA_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, YOTTA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, YOTTA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, YOTTA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, YOTTA_VALUE),
        NO_PREFIX: reciprocal(YOTTA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, YOTTA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, YOTTA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, YOTTA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, YOTTA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, YOTTA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, YOTTA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, YOTTA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, YOTTA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, YOTTA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, YOTTA_VALUE),

    },

    ZETTA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, ZETTA_VALUE),
        ZETTA_PREFIX: SELF,
        EXA_PREFIX: float_quotient(EXA_VALUE, ZETTA_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, ZETTA_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, ZETTA_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, ZETTA_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, ZETTA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, ZETTA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, ZETTA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, ZETTA_VALUE),
        NO_PREFIX: reciprocal(ZETTA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, ZETTA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, ZETTA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, ZETTA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, ZETTA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, ZETTA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, ZETTA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, ZETTA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, ZETTA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, ZETTA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, ZETTA_VALUE),

    },

    EXA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, EXA_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, EXA_VALUE),
        EXA_PREFIX: SELF,
        PETA_PREFIX: float_quotient(PETA_VALUE, EXA_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, EXA_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, EXA_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, EXA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, EXA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, EXA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, EXA_VALUE),
        NO_PREFIX: reciprocal(EXA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, EXA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, EXA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, EXA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, EXA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, EXA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, EXA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, EXA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, EXA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, EXA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, EXA_VALUE),

    },

    PETA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, PETA_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, PETA_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, PETA_VALUE),
        PETA_PREFIX: SELF,
        TERA_PREFIX: float_quotient(TERA_VALUE, PETA_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, PETA_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, PETA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, PETA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, PETA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, PETA_VALUE),
        NO_PREFIX: reciprocal(PETA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, PETA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, PETA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, PETA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, PETA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, PETA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, PETA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, PETA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, PETA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, PETA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, PETA_VALUE),

    },

    TERA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, TERA_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, TERA_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, TERA_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, TERA_VALUE),
        TERA_PREFIX: SELF,
        GIGA_PREFIX: float_quotient(GIGA_VALUE, TERA_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, TERA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, TERA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, TERA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, TERA_VALUE),
        NO_PREFIX: reciprocal(TERA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, TERA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, TERA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, TERA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, TERA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, TERA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, TERA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, TERA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, TERA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, TERA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, TERA_VALUE),

    },

    GIGA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, GIGA_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, GIGA_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, GIGA_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, GIGA_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, GIGA_VALUE),
        GIGA_PREFIX: SELF,
        MEGA_PREFIX: float_quotient(MEGA_VALUE, GIGA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, GIGA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, GIGA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, GIGA_VALUE),
        NO_PREFIX: reciprocal(GIGA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, GIGA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, GIGA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, GIGA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, GIGA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, GIGA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, GIGA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, GIGA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, GIGA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, GIGA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, GIGA_VALUE),

    },

    MEGA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, MEGA_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, MEGA_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, MEGA_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, MEGA_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, MEGA_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, MEGA_VALUE),
        MEGA_PREFIX: SELF,
        KILO_PREFIX: float_quotient(KILO_VALUE, MEGA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, MEGA_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, MEGA_VALUE),
        NO_PREFIX: reciprocal(MEGA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, MEGA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, MEGA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, MEGA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, MEGA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, MEGA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, MEGA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, MEGA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, MEGA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, MEGA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, MEGA_VALUE),

    },

    KILO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, KILO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, KILO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, KILO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, KILO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, KILO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, KILO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, KILO_VALUE),
        KILO_PREFIX: SELF,
        HECTO_PREFIX: float_quotient(HECTO_VALUE, KILO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, KILO_VALUE),
        NO_PREFIX: reciprocal(KILO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, KILO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, KILO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, KILO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, KILO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, KILO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, KILO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, KILO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, KILO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, KILO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, KILO_VALUE),

    },

    HECTO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, HECTO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, HECTO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, HECTO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, HECTO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, HECTO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, HECTO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, HECTO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, HECTO_VALUE),
        HECTO_PREFIX: SELF,
        DECA_PREFIX: float_quotient(DECA_VALUE, HECTO_VALUE),
        NO_PREFIX: reciprocal(HECTO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, HECTO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, HECTO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, HECTO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, HECTO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, HECTO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, HECTO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, HECTO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, HECTO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, HECTO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, HECTO_VALUE),

    },

    DECA_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, DECA_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, DECA_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, DECA_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, DECA_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, DECA_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, DECA_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, DECA_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, DECA_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, DECA_VALUE),
        DECA_PREFIX: SELF,
        NO_PREFIX: reciprocal(DECA_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, DECA_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, DECA_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, DECA_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, DECA_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, DECA_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, DECA_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, DECA_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, DECA_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, DECA_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, DECA_VALUE),

    },

    NO_PREFIX: {

        YOTTA_PREFIX: YOTTA_VALUE,
        ZETTA_PREFIX: ZETTA_VALUE,
        EXA_PREFIX: EXA_VALUE,
        PETA_PREFIX: PETA_VALUE,
        TERA_PREFIX: TERA_VALUE,
        GIGA_PREFIX: GIGA_VALUE,
        MEGA_PREFIX: MEGA_VALUE,
        KILO_PREFIX: KILO_VALUE,
        HECTO_PREFIX: HECTO_VALUE,
        DECA_PREFIX: DECA_VALUE,
        NO_PREFIX: SELF,
        DECI_PREFIX: DECI_VALUE,
        CENTI_PREFIX: CENTI_VALUE,
        MILLI_PREFIX: MILLI_VALUE,
        MICRO_PREFIX: MICRO_VALUE,
        NANO_PREFIX: NANO_VALUE,
        PICO_PREFIX: PICO_VALUE,
        FEMTO_PREFIX: FEMTO_VALUE,
        ATTO_PREFIX: ATTO_VALUE,
        ZEPTO_PREFIX: ZEPTO_VALUE,
        YOCTO_PREFIX: YOCTO_VALUE,

    },

    DECI_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, DECI_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, DECI_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, DECI_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, DECI_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, DECI_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, DECI_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, DECI_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, DECI_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, DECI_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, DECI_VALUE),
        NO_PREFIX: reciprocal(DECI_VALUE),
        DECI_PREFIX: SELF,
        CENTI_PREFIX: float_quotient(CENTI_VALUE, DECI_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, DECI_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, DECI_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, DECI_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, DECI_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, DECI_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, DECI_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, DECI_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, DECI_VALUE),

    },

    CENTI_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, CENTI_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, CENTI_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, CENTI_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, CENTI_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, CENTI_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, CENTI_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, CENTI_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, CENTI_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, CENTI_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, CENTI_VALUE),
        NO_PREFIX: reciprocal(CENTI_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, CENTI_VALUE),
        CENTI_PREFIX: SELF,
        MILLI_PREFIX: float_quotient(MILLI_VALUE, CENTI_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, CENTI_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, CENTI_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, CENTI_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, CENTI_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, CENTI_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, CENTI_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, CENTI_VALUE),

    },

    MILLI_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, MILLI_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, MILLI_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, MILLI_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, MILLI_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, MILLI_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, MILLI_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, MILLI_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, MILLI_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, MILLI_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, MILLI_VALUE),
        NO_PREFIX: reciprocal(MILLI_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, MILLI_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, MILLI_VALUE),
        MILLI_PREFIX: SELF,
        MICRO_PREFIX: float_quotient(MICRO_VALUE, MILLI_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, MILLI_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, MILLI_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, MILLI_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, MILLI_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, MILLI_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, MILLI_VALUE),

    },

    MICRO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, MICRO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, MICRO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, MICRO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, MICRO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, MICRO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, MICRO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, MICRO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, MICRO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, MICRO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, MICRO_VALUE),
        NO_PREFIX: reciprocal(MICRO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, MICRO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, MICRO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, MICRO_VALUE),
        MICRO_PREFIX: SELF,
        NANO_PREFIX: float_quotient(NANO_VALUE, MICRO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, MICRO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, MICRO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, MICRO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, MICRO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, MICRO_VALUE),

    },

    NANO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, NANO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, NANO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, NANO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, NANO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, NANO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, NANO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, NANO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, NANO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, NANO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, NANO_VALUE),
        NO_PREFIX: reciprocal(NANO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, NANO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, NANO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, NANO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, NANO_VALUE),
        NANO_PREFIX: SELF,
        PICO_PREFIX: float_quotient(PICO_VALUE, NANO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, NANO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, NANO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, NANO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, NANO_VALUE),

    },

    PICO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, PICO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, PICO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, PICO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, PICO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, PICO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, PICO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, PICO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, PICO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, PICO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, PICO_VALUE),
        NO_PREFIX: reciprocal(PICO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, PICO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, PICO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, PICO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, PICO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, PICO_VALUE),
        PICO_PREFIX: SELF,
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, PICO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, PICO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, PICO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, PICO_VALUE),

    },

    FEMTO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, FEMTO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, FEMTO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, FEMTO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, FEMTO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, FEMTO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, FEMTO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, FEMTO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, FEMTO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, FEMTO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, FEMTO_VALUE),
        NO_PREFIX: reciprocal(FEMTO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, FEMTO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, FEMTO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, FEMTO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, FEMTO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, FEMTO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, FEMTO_VALUE),
        FEMTO_PREFIX: SELF,
        ATTO_PREFIX: float_quotient(ATTO_VALUE, FEMTO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, FEMTO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, FEMTO_VALUE),

    },

    ATTO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, ATTO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, ATTO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, ATTO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, ATTO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, ATTO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, ATTO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, ATTO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, ATTO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, ATTO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, ATTO_VALUE),
        NO_PREFIX: reciprocal(ATTO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, ATTO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, ATTO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, ATTO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, ATTO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, ATTO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, ATTO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, ATTO_VALUE),
        ATTO_PREFIX: SELF,
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, ATTO_VALUE),
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, ATTO_VALUE),

    },

    ZEPTO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, ZEPTO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, ZEPTO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, ZEPTO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, ZEPTO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, ZEPTO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, ZEPTO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, ZEPTO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, ZEPTO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, ZEPTO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, ZEPTO_VALUE),
        NO_PREFIX: reciprocal(ZEPTO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, ZEPTO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, ZEPTO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, ZEPTO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, ZEPTO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, ZEPTO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, ZEPTO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, ZEPTO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, ZEPTO_VALUE),
        ZEPTO_PREFIX: SELF,
        YOCTO_PREFIX: float_quotient(YOCTO_VALUE, ZEPTO_VALUE),

    },

    YOCTO_PREFIX: {

        YOTTA_PREFIX: float_quotient(YOTTA_VALUE, YOCTO_VALUE),
        ZETTA_PREFIX: float_quotient(ZETTA_VALUE, YOCTO_VALUE),
        EXA_PREFIX: float_quotient(EXA_VALUE, YOCTO_VALUE),
        PETA_PREFIX: float_quotient(PETA_VALUE, YOCTO_VALUE),
        TERA_PREFIX: float_quotient(TERA_VALUE, YOCTO_VALUE),
        GIGA_PREFIX: float_quotient(GIGA_VALUE, YOCTO_VALUE),
        MEGA_PREFIX: float_quotient(MEGA_VALUE, YOCTO_VALUE),
        KILO_PREFIX: float_quotient(KILO_VALUE, YOCTO_VALUE),
        HECTO_PREFIX: float_quotient(HECTO_VALUE, YOCTO_VALUE),
        DECA_PREFIX: float_quotient(DECA_VALUE, YOCTO_VALUE),
        NO_PREFIX: reciprocal(YOCTO_VALUE),
        DECI_PREFIX: float_quotient(DECI_VALUE, YOCTO_VALUE),
        CENTI_PREFIX: float_quotient(CENTI_VALUE, YOCTO_VALUE),
        MILLI_PREFIX: float_quotient(MILLI_VALUE, YOCTO_VALUE),
        MICRO_PREFIX: float_quotient(MICRO_VALUE, YOCTO_VALUE),
        NANO_PREFIX: float_quotient(NANO_VALUE, YOCTO_VALUE),
        PICO_PREFIX: float_quotient(PICO_VALUE, YOCTO_VALUE),
        FEMTO_PREFIX: float_quotient(FEMTO_VALUE, YOCTO_VALUE),
        ATTO_PREFIX: float_quotient(ATTO_VALUE, YOCTO_VALUE),
        ZEPTO_PREFIX: float_quotient(ZEPTO_VALUE, YOCTO_VALUE),
        YOCTO_PREFIX: SELF,

    },
    
}

# PART 2: Unit Conversions

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

PA_TO_ATM: float = reciprocal(101325)
PA_TO_BAR: float = reciprocal(sci_note(5))
PA_TO_TORR: float = reciprocal(133.322)
PA_TO_PSI: float = reciprocal(6894.76)

# Time Conversions
SEC_UNIT: str = "sec"
MIN_UNIT: str = "min"
HOUR_UNIT: str = "hr"
DAY_UNIT: str = "day"
WEEK_UNIT: str = "week"
MONTH_UNIT: str = "month"
YEAR_UNIT: str = "year"

SEC_TO_MIN: float = reciprocal(60)
SEC_TO_HR: float = float_quotient(SEC_TO_MIN, 60)
SEC_TO_DAY: float = float_quotient(SEC_TO_HR, 24)
SEC_TO_WEEK: float = float_quotient(SEC_TO_DAY, 7)
SEC_TO_MONTH: float = float_quotient(SEC_TO_DAY, float_quotient(365.24/12))
SEC_TO_YEAR: float = float_quotient(SEC_TO_DAY, 365.24)


ENERGY_CONVERSIONS: float = {

    JOULE_UNIT: {

        JOULE_UNIT: SELF,
        CAL_UNIT: JOULE_TO_CAL,
        LITER_X_ATM_UNIT: JOULE_TO_LITER_X_ATM,
        CUBIC_FT_PSI_UNIT: JOULE_TO_CUBIC_FT_PSI,
        WATT_HR_UNIT: JOULE_TO_WATT_HR,

    },

    CAL_UNIT: {

        JOULE_UNIT: reciprocal(JOULE_TO_CAL),
        CAL_UNIT: SELF,
        LITER_X_ATM_UNIT: float_quotient(JOULE_TO_CAL, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI_UNIT: float_quotient(JOULE_TO_CAL, JOULE_TO_CUBIC_FT_PSI),
        WATT_HR_UNIT: float_quotient(JOULE_TO_CAL, JOULE_TO_WATT_HR),

    },

    LITER_X_ATM_UNIT: {

        JOULE_UNIT: reciprocal(JOULE_TO_LITER_X_ATM),
        CAL_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_CAL),
        LITER_X_ATM_UNIT: SELF,
        CUBIC_FT_PSI_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_CUBIC_FT_PSI),
        WATT_HR_UNIT: float_quotient(JOULE_TO_LITER_X_ATM, JOULE_TO_WATT_HR),

    },

    CUBIC_FT_PSI_UNIT: {

        JOULE_UNIT: reciprocal(JOULE_TO_CUBIC_FT_PSI),
        CAL_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_CAL),
        LITER_X_ATM_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_LITER_X_ATM),
        CUBIC_FT_PSI_UNIT: SELF,
        WATT_HR_UNIT: float_quotient(JOULE_TO_CUBIC_FT_PSI, JOULE_TO_WATT_HR),


    },

    WATT_HR_UNIT: {

        JOULE_UNIT: reciprocal(JOULE_TO_WATT_HR),
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

        PA_UNIT: reciprocal(PA_TO_ATM),
        ATM_UNIT: SELF,
        BAR_UNIT: float_quotient(PA_TO_ATM, PA_TO_BAR),
        TORR_UNIT: float_quotient(PA_TO_ATM, PA_TO_TORR),

    },

    BAR_UNIT: {

        PA_UNIT: reciprocal(PA_TO_BAR),
        ATM_UNIT: float_quotient(PA_TO_BAR, PA_TO_ATM),
        BAR_UNIT: SELF,
        TORR_UNIT: float_quotient(PA_TO_BAR, PA_TO_TORR),
    },

    TORR_UNIT: {
        
        PA_UNIT: reciprocal(PA_TO_TORR),
        ATM_UNIT: float_quotient(PA_TO_TORR, PA_TO_ATM),
        BAR_UNIT: float_quotient(PA_TO_TORR, PA_TO_BAR),
        TORR_UNIT: SELF,
    }


}

TIME_CONVERSIONS: float = {}

LENGTH_CONVERSIONS: float = {}
