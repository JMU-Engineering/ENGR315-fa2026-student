import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

#Values
    a = 1
    b = 1 / math.sqrt(2)
    t = 1/ 4
    p = 1

    error = 1

#old values
    while error >= abs(target_error):
        a_old = a
        b_old = b
        t_old = t
        p_old = p

#Gauss-legendre 
        a = (a_old + b_old) / 2
        b = math.sqrt(a_old * b_old)
        t = t_old - p_old * (a_old - a)**2
        p = 2 * p_old

        pi_estimate = ((a + b)**2) / (4 * t)

        error = abs(math.pi - pi_estimate)

    # change this so an actual value is returned
    return pi_estimate

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
