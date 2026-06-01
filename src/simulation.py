import numpy as np

#function to calculate evapotranspiration.
#can take in numpy arrays and return  a numpy array et , with et values for all 30 days
def calculate_et(temp,wind,solar,humidity):
    et = 0.12*temp + 0.35*wind + 2.4*solar - 0.025*humidity 
    return np.maximum(0,et) 

#function to calculate water balance.

def water_balance(S,R,I,ET,D):
    S_new = S + R + I -ET - D 
    #since soil moisture can never be zero , we use the max function to ensure this.
    return np.maximum(0,S_new)


# euler simulation function
def euler_simulation(S0, rainfall, et_values, field_capacity, drainage_coeff,
                     target_moisture, irrigation_amount=5.0, h=1):
    """
    Simulate soil moisture over time using the Euler method.

    Parameters:
        S0               : float : initial soil moisture
        rainfall         : list  : daily rainfall values
        et_values        : list  : daily ET values
        field_capacity   : float : maximum soil water holding capacity
        drainage_coeff   : float : fraction of excess water lost to drainage
        target_moisture  : float : target moisture threshold for irrigation
        irrigation_amount: float : fixed irrigation applied when below target
        h                : float : time step size in days

    Returns:
        moisture_values : list : simulated soil moisture for each day
        irrigation_log  : list : irrigation applied each day
    """

    S = S0
    moisture_values = [S]
    irrigation_log  = []

    n = len(rainfall)

    for t in range(n):

        # decide irrigation for today
        if S < target_moisture:
            I = irrigation_amount
        else:
            I = 0.0

        irrigation_log.append(I)

        R  = rainfall[t]
        ET = et_values[t]

        # compute drainage
        D = drainage_coeff * max(0, S + R + I - ET - field_capacity)

        # euler step
        dS_dt = R + I - ET - D
        S = S + h * dS_dt

        # soil moisture cannot go below zero
        S = max(0, S)

        moisture_values.append(S)

    return moisture_values, irrigation_log


def rk4_simulation(S0, rainfall, et_values, field_capacity, drainage_coeff,
                   target_moisture, irrigation_amount=5.0, h=1):
    """
    Simulate soil moisture over time using the 4th-order Runge-Kutta method.

    Parameters:
        S0               : float : initial soil moisture
        rainfall         : list  : daily rainfall values
        et_values        : list  : daily ET values
        field_capacity   : float : maximum soil water holding capacity
        drainage_coeff   : float : fraction of excess water lost to drainage
        target_moisture  : float : target moisture threshold for irrigation
        irrigation_amount: float : fixed irrigation applied when below target
        h                : float : time step size in days

    Returns:
        moisture_values : list : simulated soil moisture for each day
        irrigation_log  : list : irrigation applied each day
    """

    def dS_dt(S, R, I, ET):
        D = drainage_coeff * max(0, S - field_capacity)
        return R + I - ET - D

    S = S0
    moisture_values = [S]
    irrigation_log  = []

    n = len(rainfall)

    for t in range(n):

        # decide irrigation for today based on current moisture
        I  = irrigation_amount if S < target_moisture else 0.0
        irrigation_log.append(I)

        R  = rainfall[t]
        ET = et_values[t]

        # four RK4 slope estimates
        k1 = dS_dt(S,               R, I, ET)
        k2 = dS_dt(S + h*k1/2,      R, I, ET)
        k3 = dS_dt(S + h*k2/2,      R, I, ET)
        k4 = dS_dt(S + h*k3,        R, I, ET)

        # weighted average step
        S = S + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        S = max(0, S)

        moisture_values.append(S)

    return moisture_values, irrigation_log