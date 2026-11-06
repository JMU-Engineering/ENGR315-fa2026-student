from locale import localize
import sys

from matplotlib import dates

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

#Name of the data file
data_file = "us-counties.csv"

LOCALITIES = [('Harrisonburg city', 'Virginia'),
              ('Rockingham', 'Virginia')]

WINDOW = 7  # length (in days) of the "worst period" window for Question 3


def get_locality_series(data, county, state):
    """
    Extract the date and case count series for a specific locality.

    :param data: list of (date, county, state, fips, cases, deaths) tuples
    :param county: county name exactly as it appears in the NYT file
    :param state: state name exactly as it appears in the NYT file
    :return: two parallel lists: dates (strings) and cumulative case counts (ints),
             in the order they appear in the file (the file is sorted by date)
    """
    dates = []
    cumulative  = []

    for (date, c, s, fips, cases, deaths) in data:
        if c == county and s == state:
            dates.append(date)
            cumulative.append(cases)
 
    return dates, cumulative



def get_new_cases(cumulative):


    new_cases = []
    previous = 0  # no cases before the first record
 
    for total in cumulative:
        new_cases.append(total - previous)
        previous = total
 
    return new_cases
 
 
def first_case_date(dates, cumulative):

 for i in range(len(dates)):
        if cumulative[i] > 0:
            return dates[i]
        return None
 
 
def max_new_cases_day(dates, new_cases):
    best_index = 0
    for i in range(1, len(new_cases)):
        if new_cases[i] > new_cases[best_index]:
            best_index = i
    return dates[best_index], new_cases[best_index]
 
 
def worst_seven_day_period(dates, new_cases, window=WINDOW):

    best_start = 0
    best_total = None
 
    # last valid start position leaves room for a full window
    for start in range(len(new_cases) - window + 1):
        total = 0
        for k in range(start, start + window):
            total += new_cases[k]
 
        if best_total is None or total > best_total:
            best_total = total
            best_start = start
 
    return dates[best_start], dates[best_start + window - 1], best_total

def main():
    # read the whole NYT file once
    data = parse_nyt_data(data_file)
 
    # answer all three questions for each locality
    for (county, state) in LOCALITIES:
        dates, cumulative = get_locality_series(data, county, state)
 
        if len(dates) < WINDOW:
            print('Not enough data for', county, state)
            continue
 
        new_cases = get_new_cases(cumulative)
 
        print('=' * 60)
        print(county + ', ' + state)
        print('=' * 60)
 
        # Question 1
        print('Q1: First positive COVID case:', first_case_date(dates, cumulative))
 
        # Question 2
        day, count = max_new_cases_day(dates, new_cases)
        print('Q2: Most new cases in one day:', day, '(' + str(count) + ' new cases)')
 
        # Question 3
        start, end, total = worst_seven_day_period(dates, new_cases)
        print('Q3: Worst 7-day period:', start, 'through', end,
              '(' + str(total) + ' new cases)')
        print()
 
 
if __name__ == '__main__':
    main()

    








