import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_check = ['chicago', 'new york city', 'washington']
month_check = ['all','january', 'february', 'march', 'april', 'may', 'june']
day_check = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello!\nLet\'s get some information about bike sharing in the US!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nThe cities available are: Chicago, New York City, Washington')
    city = None
    while city not in city_check:
        try:
            city = input('Please choose one of the cities mentioned: ').lower()
        except ValueError:
            print('Error: Please choose a city which is availabe')
            continue
        else:
            if city in city_check:
                break
            else:
                print('Error: Please choose a city which is availabe')
    """
    Checks if input for city is valid.
    """
    print('Cool, you chose: ', city.title())

    # TO DO: get user input for month (all, january, february, ... , june)
    print('\nThe months available are: All, January, February, March, April, May, June')
    month = None
    while month not in month_check:
        try:
            month = input('Please choose one of the months mentioned. If you do not want to set a month filter choose All: ').lower()
        except ValueError:
            print('Error: Please choose a month which is availabe')
            continue
        else:
            if month in month_check:
                break
            else:
                print('Error: Please choose a month which is availabe')
    """
    Checks if input for month is valid.
    """
    print('Cool, you chose: ', month.title())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nThe days available are: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
    day = None
    while day not in day_check:
        try:
            day = input('Please choose one of the days mentioned. If you do not want to set a day filter choose All: ').lower()
        except ValueError:
            print('Error: Please choose a day which is availabe')
            continue
        else:
            if day in day_check:
                break
            else:
                print('Error: Please choose a day which is availabe')
    """
    Checks if input for day is valid.
    """

    print('Cool, you chose: ', day.title())

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
    df = pd.read_csv(CITY_DATA[city])
    """
    selects csv file to be loaded regarding the input/selection from user.
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    """
    Converts column 'Start Time' into datetime.
    """
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    """"
    Takes month & weekday out of 'Start Time' for creating new columns
    """
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    """
    Generate output if did not want to set filter for month --> 'all'.
    """
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    """
    Generate output if did not want to set filter for day --> 'all'.
    """
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    print('\nMost common month (Jan = 1, ..., Jun = 6): ', df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print('\nMost common day of week: ', df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print('\nMost common start hour: ', df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used start station: ', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station: ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    """
    combines both criteria for the check
    """
    print('\nMost frequent combination of start and end station trip: ', df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time (in full minutes rounded down): ', int(df['Trip Duration'].sum()//60))
    """
    division by 60 to show minutes instead of seconds for better overview.
    """

    # TO DO: display mean travel time
    print('\nAverage travel time (in full minutes rounded down): ', int(df['Trip Duration'].mean()//60))
    """
    division by 60 to show minutes instead of seconds for better overview.
    """
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        df['Gender'].fillna('No Gender statement', inplace = True)
    except:
        print("GENERAL INFORMATION: There is no Gender data available for the chosen Parameters")


    df['User Type'].fillna('No User Type statement', inplace = True)
    """
    Dealing with NaN data.
    """
    # TO DO: Display counts of user types
    print('\nCounts of user types:\n',df['User Type'].value_counts())
    # TO DO: Display counts of gender
    try:
        print('\nCounts of gender:\n',df['Gender'].value_counts())
    except:
        print("\nThere is no Gender data available for calculating the counts per Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nEarliest year of birth regarding users:\n',int(df['Birth Year'].min()))
    except:
        print("\nThere is no year of birth data available for calculating most common year of birth")

    try:
        print('\nMost recent year of birth regarding users:\n',int(df['Birth Year'].max()))
    except:
        print("\nThere is no year of birth data available for calculating most recent year of birth")

    try:
        print('\nMost common year of birth regarding users:\n', int(df['Birth Year'].value_counts().idxmax()))
    except:
        print("\nThere is no year of birth data available for calculating most common year of birth")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_insights(df):
    """Displays statistics on bikeshare users."""

    print('\nDisplaying raw data...\n')
    """
    Providing raw data upon request by user
    """

    show_raw_data = input('\nIf you are interested in getting an insight of the raw data, please coose Yes, otherwise choose No\n').lower()
    if show_raw_data == ('Yes').lower():
        raw_data = 6
        while True:
            print(df.iloc[:raw_data])
            raw_data += 5
            more_data = input('\ndo you wish to see more data?\n Please enter Yes or No:\n').lower()
            if more_data == ('Yes').lower():
                continue
            if more_data != ('Yes').lower():
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_insights(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
