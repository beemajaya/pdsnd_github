import time
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib as plt

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def get_city():
        while True:
            city = input ("Which city would you like to explore?\nChicago\nNew York City\nWashington\n").lower()
            if city in (CITY_DATA.keys()):              
                return city
            else:
                print(f'Sorry, "{city.title()}" is not a valid city, please input "Chicago", "New York", or "Washington".')
            
    while True:
        city = get_city()
        city_check = input(f'Alright, let\'s explore data from {city.title()}!\nIs this correct?\nY/N: ').lower()
        while city_check not in ('y', 'n'):
            city_check = input(f'Sorry, "{city_check}" is not a valid answer, please input "Y" for "Yes" and "N" for "No".')
        if city_check == ('y'):
            break
        else:
            continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(f'Okay! Which month between January and June would you like to analyze for {city.title()}?\nUse "All" for no filter:\n').lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print(f'Sorry, "{month}" is not a valid answer, please choose between\nJanuary, February, March, April, May, June, All (no filter)')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(f'Last step! Which day of the week would you like to analyze for {city.title()} in {month.title()}?\nUse "All" for no filter:\n').lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else: 
            print(f'Sorry, "{day}" is not a valid day of the week or "All", please choose between\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All(No filter)')

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]        

        return df
    
def raw_data_display(df):
    rowId = 0
    raw_data = input('\nWould you like to see first 5 rows of the raw data? Enter yes or no\n').lower()
    while raw_data == 'yes': 
        print(df.head(rowId+5)) 
        raw_data = input('\nWould you like to see 5 more rows of the raw data? Enter yes or no\n').lower()
    else:
        print('\n Exiting this loop')


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
          
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\n Most popular month',popular_month)     

    # TO DO: display the most common day of week
          
    popular_day = df['day_of_week'].mode()[0]
    print('\n Most popular day of the week',popular_day)

    # TO DO: display the most common start hour
          
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\n Most popular hour',popular_hour)      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    mc_start = df['Start Station'].mode()[0]
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print('\n Most common start station: ',start_station)
          
    # TO DO: display most commonly used end station

    mc_end = df['End Station'].mode()[0]
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print('\n Most common end station: ',end_station)      

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
     #sum for total trip time, mean for avg trip time

    total_travel_time = np.sum(df['Travel Time'])
    totalDays = str(total_travel_time).split()[0]
    print ("\n Total travel time is:",total_travel_time)
    print("\n Total travel is %s days" %totalDays)      

    # TO DO: display mean travel time

    average_travel_time = np.mean(df['Travel Time'])
    td =average_travel_time.total_seconds()
    tm = round(td/60)
    print ("\n Average travel time in minutes",tm)      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_count = df['User Type'].value_counts()
    print ('\n Counts of user types:\n', user_count)      

    # TO DO: Display counts of gender
          
    if 'gender' in df.columns:
        gender=df['Gender'].value_counts()
        print('Gender breakdown for the users is\n',gender)
    else:
        print('\n Gender column not in data!')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
     # Provide age for riders only if birth year is present
        df['Age_2018']= (pd.to_datetime('today').year-df['Birth Year'])
        earliest = round(np.min(df['Birth Year']),0)
        youngest = round(np.min(df['Age_2018']),0)
        print ("\nThe earliest year of birth is " + str(earliest) + "\n")
        print ("\nThe youngest customer is " + str(youngest) + "\n")
        latest = round(np.max(df['Birth Year']),0)
        oldest = round(np.max(df['Age_2018']),0)
        print ("The latest year of birth is " + str(latest) + "\n")
        print ("\nThe oldest customer is " + str(oldest) + "\n")
        most_frequent= round(df['Birth Year'].mode()[0],0)
        common_age = round(df['Age_2018'].mode()[0],0)
        print ("The most frequent year of birth is " + str(most_frequent) + "\n")
        print ("\nThe most common age of customer is " + str(common_age) + "\n")
        
    else:
        print('\n Birth Year column not in data!')      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data_display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()