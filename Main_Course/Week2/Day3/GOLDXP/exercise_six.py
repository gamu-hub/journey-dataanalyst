# Exercise 6: Birthday and minutes
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations.total_seconds() method

# Instructions:

# Create a function that accepts a birthdate 
# as an argument (in the format of your choice), 
# then displays a message stating 
# how many minutes the user lived in his life. 

# importing datetime module
import datetime

def calculate_minutes_lived(birthdate):
    """ Calculate and display the number of minutes lived"""

    # using strptime given by python 
    birth_datetime = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

    # the current datetime
    current_datetime = datetime.datetime.now()

    # calculating the time difference 
    time_difference = current_datetime - birth_datetime

    # Using .total_seconds() method to calculate minutes lived dividing by 60 seconds
    minutes_lived = time_difference.total_seconds() / 60

    # Display the minute lived
    print(f"You have lived {minutes_lived} minutes.")

# call a function of the minutes lived
calculate_minutes_lived("1993-09-28")