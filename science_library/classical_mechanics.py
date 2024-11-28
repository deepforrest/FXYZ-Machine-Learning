from fundamentals_library.computations import *
from fundamentals_library.constants import *
import math

def newtonian_force(mass: float, acceleration: float):

    if mass < 0:
        
        return None
    
    return product(mass, acceleration)

def average_velocity(final_position: float, initial_position: float, final_time: float, initial_time: float) -> float:

    return float_quotient(difference(final_position, initial_position), difference(final_time, initial_time))


def average_acceleration(final_velocity: float, initial_velocity: float, final_time: float, initial_time: float) -> float:

    return float_quotient(difference(final_velocity, initial_velocity), difference(final_time, initial_time))