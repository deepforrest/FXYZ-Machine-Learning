from math_library.algebraic_functions import *
from fundamentals_library.computations import *
from fundamentals_library.constants import *


# Calculates the adjusted hourly wage earned from working with clients based on travel time (an opp. cost)

def assignment_earnings(hourly_rate: float, hours_worked: float, travel_charges: float = 0) -> float:

    work_charges: float = product(hourly_rate, hours_worked)
    
    return add(work_charges, travel_charges)


def work_time(work_hrs: float, travel_hrs: float) -> float:

    return add(work_hrs, double(travel_hrs))


def adj_travel_wage(hourly_rate: float, work_hrs: float, travel_hrs: float, travel_charge: float = 0) -> float:

    total_earnings: float = assignment_earnings(hourly_rate, work_hrs, travel_charge)
    time_worked: float = work_time(work_hrs, travel_hrs)

    return float_quotient(total_earnings, time_worked)


# Function needs thought out.  Too general, perhaps?
def marketing_roi() -> float:

    pass