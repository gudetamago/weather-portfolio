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
    total_count = 0
    total_value = 0.0
    if bool(weather_data):
        for weather in weather_data:
            total_value = total_value + float(weather)
            total_count += 1
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
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if bool(weather_data):
        minimum_value = float(weather_data[0])
        minimum_index = 0
        
        for index, item in enumerate(weather_data):
            if float(item) <= float(minimum_value):
                minimum_value = round(float(item), 1)
                minimum_index = index
            
        return (minimum_value, minimum_index)
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
        maximum_value = float(weather_data[0])
        maximum_index = 0
    
        for index, item in enumerate(weather_data):
            if float(item) >= float(maximum_value):
                maximum_value = round(float(item), 1)
                maximum_index = index
        return (maximum_value, maximum_index)
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
    
    for day, min, max in weather_data:
        lowest_temp = find_min(day)
    return lowest_temp


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
