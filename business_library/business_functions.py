from math_library.algebraic_functions import *
from math_library.fund_comp import *
from fundamentals_library.constants import *


# Calculates the adjusted hourly wage earned from working with clients based on travel time (an opp. cost)

def assignment_earnings(hourly_rate: float, hours_worked: float, travel_charges: float = 0):

    return add(product(hourly_rate, hours_worked), travel_charges)

def work_time(work_hrs: float, travel_hrs: float):

    return add(work_hrs, product(2, travel_hrs))

def adj_travel_wage(hourly_rate: float, work_hrs: float, travel_hrs: float, travel_charge: float = 0):

    return float_quotient(assignment_earnings(hourly_rate, work_hrs, travel_charge), work_time(work_hrs, travel_hrs))

def marketing_roi():

    pass