#function to calculate evapotranspiration.

def calculate_et(temp,wind,solar,humidity):
    et = 0.12*temp + 0.35*wind + 2.4*solar - 0.025*humidity 
    return max(0,et) 

#function to calculate water balance.

def water_balance(S,R,I,ET,D):
    S_new = S + R + I -ET - D 
    #since soil moisture can never be zero , we use the max function to ensure this.
    return max(0,S_new)


