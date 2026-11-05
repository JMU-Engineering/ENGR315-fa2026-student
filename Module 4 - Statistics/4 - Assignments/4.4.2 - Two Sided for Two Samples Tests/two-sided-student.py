import numpy as np
from scipy.stats import ttest_ind

"""
Two Sided Tests for Two Samples

Complete two_sided_tests() below. Each file holds one sample of numbers (one per line). The function compares the
first file of the first list with the first file of the second list, the second with the second, and so on, using a
two-sided t-test. It returns the pairs of file names where the null hypothesis (the means are equal) is rejected.

Use Welch's t-test (equal_var=False in ttest_ind) because the two samples in a pair may have different sizes and spreads.

Your function is tested on different random files than the ones in the self-check at the bottom of this
file, so it must use every parameter.

Submit this file to Gradescope.
"""


def write_to_csv(filename: str, data):
    """
    Write an array of data to a file
    :param filename: Name of file to be written
    :param data: An array type object for data to be written to file
    :return: None
    """
    try:
        file = open(filename, 'w')
    except FileNotFoundError:
        print('Could not open file ', filename, ' error!!')
        return

    for a in data:
        file.writelines(str(a) + '\n')

    file.close()


def two_sided_tests(_files1: list, _files2: list, _alpha: float):

    reject_null_hypothesis = []

    # Loop through each pair of files
    for i in range(len(_files1)):

        # Load data from both files
        data1 = np.loadtxt(_files1[i])
        data2 = np.loadtxt(_files2[i])

        # Perform a two-sided Welch's t-test
        t_stat, p_value = ttest_ind(data1, data2, equal_var=False)

        # Check whether to reject the null hypothesis
        if p_value < _alpha:
            reject_null_hypothesis.append((_files1[i], _files2[i]))

    return reject_null_hypothesis


if __name__ == "__main__":
    # Use this section to check your work. It is not graded and is not run by Gradescope.
    # The random seed makes the files the same every time it is run.
    np.random.seed(315)

    # number of samples for each file
    num_samples = 100
    std = 1

    # two samples from the same distribution, then samples that are well apart from each other
    write_to_csv('equal1.txt', np.random.normal(loc=0, scale=std, size=num_samples))
    write_to_csv('equal2.txt', np.random.normal(loc=0, scale=std, size=num_samples))
    write_to_csv('lesser1.txt', np.random.normal(loc=-1.0, scale=std, size=num_samples))
    write_to_csv('lesser2.txt', np.random.normal(loc=-2.0, scale=std, size=num_samples))
    write_to_csv('greater1.txt', np.random.normal(loc=1.0, scale=std, size=num_samples))
    write_to_csv('greater2.txt', np.random.normal(loc=2.0, scale=std, size=num_samples))

    # comparing each file with itself. The means cannot differ, so no pairs should be returned
    same_files = ['lesser1.txt', 'greater1.txt', 'equal1.txt']
    print('Same files. Expected: []. Result: ', two_sided_tests(_files1=same_files, _files2=same_files, _alpha=0.05))

    # file 1 of the first list is compared with file 1 of the second list, and so on
    first_files = ['lesser1.txt', 'lesser1.txt', 'greater1.txt', 'equal1.txt', 'equal1.txt']
    second_files = ['lesser2.txt', 'lesser1.txt', 'greater2.txt', 'lesser1.txt', 'equal2.txt']
    print('Different files. Expected: [(\'lesser1.txt\', \'lesser2.txt\'), (\'greater1.txt\', \'greater2.txt\'), '
          '(\'equal1.txt\', \'lesser1.txt\')]')
    print('Result: ', two_sided_tests(_files1=first_files, _files2=second_files, _alpha=0.05))
