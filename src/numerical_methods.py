#finding the irrigation needed to be done on zone C to achieve target moisture (day 1)
#Equation that we are trying to solve.
#f(I) = S_current + I - ET - S_target = 0

def bisection(f,a,b,tolerance=1e-6,max_iter=100):
    """ 
    Root finding function using bisection method.
    Parameters:
        f  : function : the actual function that we are trying to solve.
        a  : float    : the lower interval
        b  : float : the upper interval
        tolerance : float : the error that can be tolerated , default = 1e-6
        max_iter : int : total number of iterations

    returns root,iterations and error
    """
    if (f(a) * f(b) > 0 ):
        print("Error!f(a) and f(b) must have different signs.")
        return None , None , None
    
    iterations = 0

    while iterations < max_iter:
        #find the midpoint , to try and narrow which half has the root.
        midpoint = (a+b)/2

        #assume the error is half the interval
        error = (b-a)/2

        #if error is less than tolerance , break
        if error < tolerance:
            break

        if ( f(a) * f(midpoint) < 0 ):
            b = midpoint
        else:
            a=midpoint
        
        iterations+=1


    return midpoint,iterations,error


#using the newton_raphson method to calculate the amount of irrigation needed to 
#attain target soil moisture.

def newton_raphson(f,f_prime,initial_guess,tolerance=1e-6,max_iter=100):
    """
    Find the root of function f using the Newton-Raphson method.

    Parameters:
        f               : function : the function whose root we are finding
        f_prime         : function : the derivative of f
        initial_guess   : float   : starting point for the iteration
        tolerance       : float   : acceptable error (default 1e-6)
        max_iterations  : int     : maximum number of iterations allowed

    Returns:
        root       : float : estimated root
        iterations : int   : number of iterations taken
        error      : float : final error estimate
    """

    x= initial_guess
    
    iterations=0

    while iterations<max_iter:

        fx=f(x)
        fpx=f_prime(x)

        #check if derivative is zero
        if(fpx == 0):
            print("Error,derivative is zero, newton_raphson cannot continue.\n")
            return None , None , None

        #newton_raphson formula
        x_new = x - (fx/fpx)

        error = abs(x-x_new)

        x = x_new
        iterations += 1

        if error < tolerance:
            break

    return x,iterations,error


#secant method.

def secant(f, x0, x1, tolerance=1e-6, max_iter=100):
    """
    Find the root of function f using the Secant method.

    Parameters:
        f         : function : the function whose root we are finding
        x0        : float   : first initial guess
        x1        : float   : second initial guess
        tolerance : float   : acceptable error (default 1e-6)
        max_iter  : int     : maximum number of iterations allowed

    Returns:
        root       : float : estimated root
        iterations : int   : number of iterations taken
        error      : float : final error estimate
    """

    iterations = 0

    while iterations < max_iter:

        fx0 = f(x0)
        fx1 = f(x1)

        # check if denominator is zero to avoid division by zero
        if fx1 - fx0 == 0:
            print("Error: division by zero. Secant method cannot continue.")
            return None, None, None

        # secant formula
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # compute error as change between iterations
        error = abs(x_new - x1)

        # update points for next iteration
        x0 = x1
        x1 = x_new

        iterations += 1

        if error < tolerance:
            break

    return x1, iterations, error

def trapezoidal(f_values, h=1):
    """
    Estimate the area under a curve using the trapezoidal rule.

    Parameters:
        f_values : list : function values at each point
        h        : float : step size between points (default 1 day)

    Returns:
        area : float : estimated area under the curve
    """
    n = len(f_values)
    area = f_values[0] + f_values[n-1]

    for i in range(1, n-1):
        area += 2 * f_values[i]

    area = (h/2) * area
    return area


# simpsons rule
def simpsons(f_values, h=1):
    """
    Estimate the area under a curve using Simpsons rule.
    Requires an even number of intervals (odd number of points).

    Parameters:
        f_values : list : function values at each point
        h        : float : step size between points (default 1 day)

    Returns:
        area : float : estimated area under the curve
    """
    n = len(f_values)

    # simpson's rule requires even number of intervals
    if (n-1) % 2 != 0:
        print("Warning: Simpson's rule requires even number of intervals.")
        print("Dropping last point to make it even.")
        f_values = f_values[:-1]
        n = len(f_values)

    area = f_values[0] + f_values[n-1]

    for i in range(1, n-1):
        if i % 2 == 0:
            area += 2 * f_values[i]
        else:
            area += 4 * f_values[i]

    area = (h/3) * area
    return area

# gaussian elimination
def gaussian_elimination(A, b):
    """
    Solve the linear system Ax = b using Gaussian elimination
    with back substitution.

    Parameters:
        A : list of lists : coefficient matrix
        b : list          : right hand side vector

    Returns:
        x : list : solution vector
    """
    n = len(b)

    # create augmented matrix [A|b]
    augmented = []
    for i in range(n):
        row = A[i][:] + [b[i]]
        augmented.append(row)

    # forward elimination
    for col in range(n):

        # find pivot - largest value in current column
        max_row = col
        for row in range(col + 1, n):
            if abs(augmented[row][col]) > abs(augmented[max_row][col]):
                max_row = row

        # swap current row with pivot row
        augmented[col], augmented[max_row] = augmented[max_row], augmented[col]

        # check if pivot is zero
        if augmented[col][col] == 0:
            print("Error: matrix is singular, no unique solution exists.")
            return None

        # eliminate entries below pivot
        for row in range(col + 1, n):
            factor = augmented[row][col] / augmented[col][col]
            for j in range(col, n + 1):
                augmented[row][j] = augmented[row][j] - factor * augmented[col][j]

    # back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - augmented[i][j] * x[j]
        x[i] = x[i] / augmented[i][i]

    return x
