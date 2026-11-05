import numpy as np
from scipy.stats import norm, chisquare

"""
Chi-Square Goodness of Fit

Complete the three functions below. They follow the Module 5.2 lecture examples: chi-square-gof-categorical.py for
counts in categories, and chi-square-dist-fit.py for binning samples and testing them against a normal distribution.

Your functions are tested on different random data than the examples at the bottom of this file, so they must work
for any data they are given.

Submit this file to Gradescope.
"""


def categorical_test(_observed, _expected, _alpha):
    """
    Chi-square goodness of fit test on counts in categories
    """
    chi_stat = None
    p_value = None
    reject = None

    # YOUR CODE HERE #
    chi_stat, p_value = chisquare(_observed, f_exp=_expected)
    reject = p_value < _alpha

    return chi_stat, p_value, reject


def expected_normal_counts(_bins, _mu, _std, _num_samples):
    """
    Expected number of samples in each bin
    """
    expected_counts = None

    # YOUR CODE HERE #
    probabilities = np.diff(norm.cdf(_bins, loc=_mu, scale=_std))
    expected_counts = probabilities * _num_samples

    return expected_counts


def normal_fit_test(_samples, _alpha):
    """
    Test whether samples could come from a normal distribution
    """
    chi_stat = None
    p_value = None
    reject = None

    # YOUR CODE HERE #

    # Step 1: Fit normal distribution
    fitted_mean, fitted_std = norm.fit(_samples)

    # Step 2: Create bin edges
    bins = np.r_[-np.inf, np.linspace(fitted_mean - 2 * fitted_std,
                                     fitted_mean + 2 * fitted_std, 9), np.inf]

    # Step 3: Calculate observed counts
    observed_counts, _ = np.histogram(_samples, bins=bins)

    # Step 4: Calculate expected counts
    expected_counts = expected_normal_counts(
        bins, fitted_mean, fitted_std, len(_samples)
    )

    # Step 5: Perform chi-square test
    chi_stat, p_value = chisquare(
        observed_counts, f_exp=expected_counts, ddof=2
    )

    reject = p_value < _alpha

    return chi_stat, p_value, reject



if __name__ == "__main__":
    # Use this section to check your work. It is not graded and is not run by Gradescope.
    # The random seed makes the samples the same every time it is run.
    np.random.seed(315)

    """
    Part 1: the bag of candy from lecture. 5 flavors, so DoF = 4
    """
    candy_observed = [180, 250, 120, 225, 225]
    candy_expected = [200, 200, 200, 200, 200]
    print('Candy. Expected: (52.75, 9.6e-11, True). Result:', categorical_test(candy_observed, candy_expected, 0.05))

    # a penny flipped 87 times
    penny_observed = [46, 41]
    penny_expected = [43.5, 43.5]
    print('Penny. Expected: (0.287, 0.592, False). Result:', categorical_test(penny_observed, penny_expected, 0.05))

    """
    Part 2: expected counts for the bins used in lecture (Yale SAT example)
    """
    bins = np.r_[-np.inf, np.linspace(-2, 2, 9), np.inf]
    print('Expected counts. Expected: [4.55, 8.81, 18.37, 29.98, 38.29, 38.29, 29.98, 18.37, 8.81, 4.55]. Result:',
          expected_normal_counts(bins, 0, 1, 200))

    """
    Part 3: test samples against a fitted normal distribution
    """
    normal_samples = np.random.normal(loc=10, scale=3, size=500)
    print('Normal samples. Expected: (6.281, 0.507, False). Result:', normal_fit_test(normal_samples, 0.05))

    exponential_samples = np.random.exponential(scale=3, size=500)
    print('Exponential samples. Expected: (203.4, 2.2e-40, True). Result:', normal_fit_test(exponential_samples, 0.05))
