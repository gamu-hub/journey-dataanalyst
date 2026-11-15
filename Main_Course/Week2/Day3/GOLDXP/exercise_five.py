
"""
Exercise 5: Amount of Time Left Until January 1st.

Calculate and display the time remaining until January 1st
of the next year using the datetime module.
"""

import datetime


def time_until_january_first():
    """Calculate and display the time left until January 1st."""

    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Create a datetime object for January 1st of next year
    next_year = current_datetime.year + 1
    january_first = datetime.datetime(next_year, 1, 1)

    # Calculate the time difference
    time_difference = january_first - current_datetime

    # Display the remaining time
    print(time_difference)


# Call the function
time_until_january_first()
