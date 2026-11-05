import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1 / math.sqrt(2)
<<<<<<< Updated upstream
t = 1/4
=======
t = 1 / 4
>>>>>>> Stashed changes
p = 1

# perform 10 iterations of this loop
for i in range(1, 11):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """
    new_a = (a + b) / 2
    new_b = math.sqrt(a * b)
    new_t = t - p * (a - new_a) ** 2
    new_p = 2 * p

    # update the variables for the next iteration
    a = new_a
    b = new_b
    t = new_t
    p = new_p

<<<<<<< Updated upstream
    a_old = a
    b_old = b
    t_old = t
    p_old = p

    a = (a_old + b_old) / 2
    b = math.sqrt(a_old * b_old)
    t = t_old - p_old * (a_old - b_old) ** 2 / 4
    p = 2 * p_old
=======
>>>>>>> Stashed changes

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
<<<<<<< Updated upstream
pi_estimate = ((a+b)**2) / (4 * t)
=======
pi_estimate = ((a + b) ** 2) / (4 * t)
>>>>>>> Stashed changes

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))