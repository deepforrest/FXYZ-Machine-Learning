from fxyz_ml_math_stats import *
from fxyz_ml_unit_testers import *

test_arith_seq_arr = build_arithmethic_sequence(-293, 10/3, 75)
test_geo_seq_arr = build_geometric_sequence(2, 1/3, 0)

print("Arithmetic:", test_arith_seq_arr, "\n\nGeometric:", test_geo_seq_arr)