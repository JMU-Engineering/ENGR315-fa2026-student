import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path ="data/covid/us-counties.csv/"):
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
#Parse through the entire .csv dataset 

covid_data = parse_nyt_data("data/covid/us-counties.csv")

# Filter the data to only get Harrisonburg and Rockingham County

harrisonburg_data = [] #create empty list for Harrisonburg data
rockingham_data = [] #create empty list for Rockingham County data

#Using a for loop to find Harrisonburg city and Rockingham County and appending them to a new list
for entry in covid_data:

    county = entry[1] #Collecting county name and creating a list
    state = entry [2] #Collecting state name and creating a list

    if county == 'Harrisonburg city' and state == "Virginia":
        harrisonburg_data.append(entry) #append list if the entry matches Harrisonburg city and Virginia

    if county == 'Rockingham' and state == "Virginia":
        rockingham_data.append(entry) #append list if the entry matches Rockingham County and Virginia

#Question 1: When was the first positive case in Harrisonburg? In Rockingham County?

#Create a function to find the first positive case in a given dataset
def first_positive_case(location_data):

#Use a for loop to iterate through the location data to find when cases > 0
    for entry in location_data:

        date = entry[0] #get the date of the current entry
        cases = entry[4] #get the total number of cases for the current entry

        if cases > 0:
            return date

harrisonburg_first_case = first_positive_case(harrisonburg_data) #creating variable for Harrisonburg's first positive case
rockingham_first_case = first_positive_case(rockingham_data)

print("The first positive case in Harrisonburg was:", harrisonburg_first_case)
print("The first positive case in Rockingham County was:", rockingham_first_case)

#Finding the number of new cases each day
#The cases are cumulative, so new cases = today's cases - yesterday's cases

#Question 2: What is the date with the greatest number of new cases?

#find number of new cases each day
#Creating a function to use to calculate the number of new cases each day
def calculate_new_cases(location_data):
    daily_cases = [] #create an empty list to store daily new cases

    previous_cases = 0 #start with zero previous cases

    #iterate through each entry in the location data to calculate new cases
    for entry in location_data:
        date = entry[0] #get the date
        total_cases = entry[4] #get the total number of cases

        new_cases = total_cases - previous_cases #find the number of new cases

        daily_cases.append((date, new_cases)) #append the date and number of new cases to this list

        previous_cases = total_cases #reset previous cases to the current total

    return daily_cases
    

harrisonburg_new_cases = calculate_new_cases(harrisonburg_data) #calculate new cases for Harrisonburg
rockingham_new_cases = calculate_new_cases(rockingham_data) #calculate new cases for Rockingham County

#Know we know the number of new cases each day, we can find the date with the greatest number of new cases
#Create a function to use to
def find_greatest_new_cases(daily_cases):

    greatest_cases = 0 #start with zero greatest cases
    greatest_date = "" #create a string to store the date

#use a for loop to iterate through each daily case entry
    for entry in daily_cases:

        date = entry[0] #get the date from the current entry
        new_cases = entry[1] #get the number of new cases from the current entry

        if new_cases > greatest_cases: #check if the current number of new cases is greater than the greatest number of new cases found so far
            greatest_cases = new_cases #update the greatest number of new cases
            greatest_date = date #update the date with the greatest number of new cases

    return greatest_date, greatest_cases

harrisonburg_greatest = find_greatest_new_cases(harrisonburg_new_cases) 
rockingham_greatest = find_greatest_new_cases(rockingham_new_cases)

print("The date with the greatest number of new cases in Harrisonburg was:", harrisonburg_greatest[0], "Number of new cases:", harrisonburg_greatest[1])
print("The date with the greatest number of new cases in Rockingham County was:", rockingham_greatest[0], "Number of new cases:", rockingham_greatest[1])

#What was the worst seven-day period in Harrisonburg city for new COVID cases? What period in Rockingham County? These are the seven-day periods when the number of new cases was maximal. 
#Check every seven-day period to find the worst consecutive seven-day period
#The function find_worst_seven_day will iterate through all possible seven-day periods and return the start date, end date, and total number of new cases for the worst period.
def find_worst_seven_day(daily_cases):

    greatest_total = 0 #start with 0
    start_date = "" #create a string to store the start date of the worst seven-day period
    end_date = "" #create a string to store the end date of the worst seven-day period

    #iterate through all possible seven-day periods, use i as the starting index of the period and subtract 6 to get the ending index
    for i in range(len(daily_cases) - 6):

        seven_day_total = 0 #start with 0

        #Use a for loop. Starting with day i, go through 7 days and add the number of new cases for each day to the seven-day total
        for j in range(i, i + 7): 
            seven_day_total = seven_day_total + daily_cases[j][1]
            #[j]is index of the current day within the seven-day period and [1] is the number of new cases for that day. This line adds up the number of new cases for each day within the seven-day period

        if seven_day_total > greatest_total: #check if the current seven-day total is greater than the greatest total found so far

            greatest_total = seven_day_total #update the greatest total
            start_date = daily_cases[i][0] #update the start date of the worst seven-day period
            end_date = daily_cases[i + 6][0] #update the end date of the worst seven-day period

    return start_date, end_date, greatest_total

harrisonburg_worst_seven_day = find_worst_seven_day(harrisonburg_new_cases)
rockingham_worst_seven_day = find_worst_seven_day(rockingham_new_cases)

print("The worst seven-day period in Harrisonburg was:", harrisonburg_worst_seven_day[0], "to", harrisonburg_worst_seven_day[1], "Number of new cases:", harrisonburg_worst_seven_day[2])
print("The worst seven-day period in Rockingham County was:", rockingham_worst_seven_day[0], "to", rockingham_worst_seven_day[1], "Number of new cases:", rockingham_worst_seven_day[2])