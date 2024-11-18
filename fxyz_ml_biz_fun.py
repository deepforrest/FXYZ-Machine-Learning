# Calculates the adjusted hourly wage earned from working with clients based on travel time (an opp. cost)
def adj_travel_wage(wage: float, work_time_hrs: float, travel_time_hrs: float, travel_charge: float = 0):

    return float_quotient(add(product(wage, work_time_hrs), travel_charge), add(work_time_hrs, product(2, travel_time_hrs)))


def marketing_roi():

    pass

def assignment_earnings(hourly_charges: float, hours_worked: float, travel_charges: float = 0):

    return add(product(hourly_charges, hours_worked), travel_charges)