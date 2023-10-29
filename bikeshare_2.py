import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Please enter the city you want to explore: Chicago, New York City or Washington")
    city = input().lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Invalid input. Please try again.")
        city = input().lower()
    print("You have chosen to explore: ", city.title())



    # get user input for month (all, january, february, ... , june)
    print("Please enter the month you want to explore: January, February, March, April, May, June or all")
    month = input().lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("Invalid input. Please try again.")
        month = input().lower()
    print("You have chosen to explore: ", month.title())


    # get user input for day of week (all, monday, tuesday, ... sunday)
    print("Please enter the day you want to explore: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all")
    day = input().lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']:
        print("Invalid input. Please try again.")
        day = input().lower()
    print("You have chosen to explore: ", day.title())


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    if month != 'all':
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()

        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if 'month' in df.columns:
        most_common_month = df['month'].mode()[0]
    else:
        most_common_month = 'N/A'
    print("The most common month is: ", most_common_month)


    # display the most common day of week
    if 'day' in df.columns:
        most_common_day = df['day'].mode()[0]
    else:
        most_common_day = 'N/A'
    print("The most common day is: ", most_common_day)

    # display the most common start hour
    if 'hour' in df.columns:
        most_common_start_hour = df['hour'].mode()[0]
    else:
        most_common_start_hour = 'N/A'
    print("The most common start hour is: ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]
    print("The most common used start station is: ", most_common_used_start_station)

    # display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]
    print("The most common used end station is: ", most_common_used_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df['Start Station'] + df['End Station'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].count()
    print("The count of user types is: ", count_user_types)

    # Display counts of gender if the gender field exists
    if 'Gender' in df.columns:
        count_gender = df['Gender'].count()
        print("The count of genders is: ", count_gender)
    else:
        print('Gender data is not available for this city.')


    # Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    print("The earliest year of birth is: ", earliest_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
