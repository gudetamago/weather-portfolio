import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    formatted_date = date.strftime("%A %d %B %Y")
    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    celcius = ( float(temp_in_fahrenheit) - 32) * 5/9
    return round(celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total_count = len(weather_data)
    total_value = 0.0
    if bool(weather_data):
        total_value = sum( float(weather) for weather in weather_data)
        average = total_value / total_count
        return average
    else:
        return None


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    
    with open(csv_file) as csv_data:      
        csv_reader = csv.reader(csv_data)
        next(csv_reader) # skip headers (first row)
        for row in csv_reader:
            if row:
                row[1] = int(row[1])
                row[2] = int(row[2])
                data.append(row)
    return data

def find_extreme_in_list(weather_data, max=True):
    """Finds the extreme value in a list of numbers.

    Args:
        weather_data: A list of numbers.
        max: A boolean indicating whether to find the maximum (True) or minimum (False).
    Returns:
        The extreme value and its position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    extreme_value = float(weather_data[0])
    extreme_index = 0
        
    for index, item in enumerate(weather_data):
        if (max and float(item) >= extreme_value) or (not max and float(item) <= extreme_value):
            extreme_value = round(float(item), 1)
            extreme_index = index
            
    return (extreme_value, extreme_index)
    
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if bool(weather_data):
        return find_extreme_in_list(weather_data, max=False)
    else:
        minimum_value = ()
        return minimum_value
    


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if bool(weather_data):
        return find_extreme_in_list(weather_data, max=True)
    else:
        maximum_value = ()
        return maximum_value


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    total_days = len(weather_data)
    list_of_mins = []
    list_of_max = []
    total_mins = 0.0
    total_max = 0.0

    # Do everything in Celcius
    for day in weather_data:
        list_of_mins.append( convert_f_to_c(day[1]))
        list_of_max.append( convert_f_to_c(day[2]))
        
    total_mins = sum(list_of_mins)
    total_max = sum(list_of_max)
    
    
    lowest_temp = find_min(list_of_mins)
    display_min_temp = format_temperature(lowest_temp[0])
    date_lowest_temp = convert_date(weather_data[lowest_temp[1]][0])
    
    highest_temp = find_max(list_of_max)
    display_max_temp = format_temperature(highest_temp[0])
    date_highest_temp = convert_date(weather_data[highest_temp[1]][0])
    
    average_low = format_temperature(round(total_mins / total_days, 1))
    average_high = format_temperature(round(total_max / total_days, 1))
    
    summary = f"{total_days} Day Overview\n"
    summary += f"  The lowest temperature will be {display_min_temp}, and will occur on {date_lowest_temp}.\n"
    summary += f"  The highest temperature will be {display_max_temp}, and will occur on {date_highest_temp}.\n"
    summary += f"  The average low this week is {average_low}.\n"
    summary += f"  The average high this week is {average_high}.\n"
    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for day in weather_data:
        date = convert_date(day[0])
        min = format_temperature(convert_f_to_c(day[1]))
        max = format_temperature(convert_f_to_c(day[2]))
        summary = summary + "---- " + date + " ----\n  Minimum Temperature: " + min + "\n  Maximum Temperature: " + max + "\n\n"
    return summary

