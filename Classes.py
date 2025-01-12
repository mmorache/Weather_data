import requests
from pkg_resources import non_empty_lines

#Using a Class to hold the API call requests.
class api_calls:
    def __init__(self, year_2023, year_2022, year_2021, year_2020, year_2019):
        self.year_2023 = requests.get(url = "https://archive-api.open-meteo.com/v1/archive?latitude=44.08&longitude=-115.62&start_date=2023-09-11&end_date=2023-09-11&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch")
        self.year_2022 = requests.get(url = "https://archive-api.open-meteo.com/v1/archive?latitude=44.08&longitude=-115.62&start_date=2022-09-11&end_date=2022-09-11&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch")
        self.year_2021 = requests.get(url = "https://archive-api.open-meteo.com/v1/archive?latitude=44.08&longitude=-115.62&start_date=2021-09-11&end_date=2021-09-11&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch")
        self.year_2020 = requests.get(url = "https://archive-api.open-meteo.com/v1/archive?latitude=44.08&longitude=-115.62&start_date=2020-09-11&end_date=2020-09-11&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch")
        self.year_2019 = requests.get(url = "https://archive-api.open-meteo.com/v1/archive?latitude=44.08&longitude=-115.62&start_date=2019-09-11&end_date=2019-09-11&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch")

    def years(self):
        return {
            "year_2023": self.year_2023.json(),
            "year_2022": self.year_2022.json(),
            "year_2021": self.year_2021.json(),
            "year_2020": self.year_2020.json(),
            "year_2019": self.year_2019.json()
        }
#creating instance so I can call it in my method below        }
api_instance = api_calls(2023, 2022, 2021, 2020, 2019)
api_dict = api_instance.years()


#The following Class houses part C1 and C2 of the task.
class weather_stats:
    def __init__(self):
        self.instance_api = api_calls(2023, 2022, 2021, 2020, 2019)
        self.latitude = 44.08
        self.longitude = -115.62
        self.month = 9
        self.day = 11
        self.year = 2023
        self.avg_temp = 0
        self.min_temp = 0
        self.max_temp = 0
        self.avg_wind_speed = 0
        self.min_wind_speed = 0
        self.max_wind_speed = 0
        self.precip = 0
        self.min_precip = 0
        self.max_precip = 0

# This method creates a dictionary with just the temperature.
    def temp_data(self, temp_2023, temp_2022, temp_2021, temp_2020, temp_2019, temp_dict=None):
        temp_dict = {
            "temp_2023":api_dict["year_2023"]["daily"]["temperature_2m_mean"],
            "temp_2022":api_dict["year_2022"]["daily"]["temperature_2m_mean"],
            "temp_2021":api_dict["year_2021"]["daily"]["temperature_2m_mean"],
            "temp_2020":api_dict["year_2020"]["daily"]["temperature_2m_mean"],
            "temp_2019":api_dict["year_2019"]["daily"]["temperature_2m_mean"],
        }
        return temp_dict

# This method takes the temperature dictionary, extracts just the values, converts them to floats, then averages the temperature.
    def mean_temp(self):
        temp_dict = self.temp_data('temp_2023', 'temp_2022', 'temp_2021', 'temp_2020', 'temp_2019')
        temp_values = [float(value[0]) for value in temp_dict.values()]
        avg_temp = sum(temp_values) / len(temp_values)
        return avg_temp

# This method creates a dictionary with just the wind speed.
    def wind_data(self, wind_2023, wind_2022, wind_2021, wind_2020, wind_2019, wind_dict=None):
        wind_dict = {
            "wind_2023":api_dict["year_2023"]["daily"]["wind_speed_10m_max"],
            "wind_2022":api_dict["year_2022"]["daily"]["wind_speed_10m_max"],
            "wind_2021":api_dict["year_2021"]["daily"]["wind_speed_10m_max"],
            "wind_2020":api_dict["year_2020"]["daily"]["wind_speed_10m_max"],
            "wind_2019":api_dict["year_2019"]["daily"]["wind_speed_10m_max"],
        }
        return wind_dict

# This method takes the wind dictionary, extracts just the values, converts them to floats, then determines the max wind speed.
    def max_wind(self):
        wind_dict = self.wind_data('temp_2023', 'temp_2022', 'temp_2021', 'temp_2020', 'temp_2019')
        wind_values = [float(value[0]) for value in wind_dict.values()]
        max_wind_spd = max(wind_values)
        return max_wind_spd


# This method creates a dictionary with just the precipitation.
    def precip_data(self, precip_2023, precip_2022, precip_2021, precip_2020, precip_2019=None, precip_dict=None):
        precip_dict = {
            "precip_2023":api_dict["year_2023"]["daily"]["precipitation_sum"],
            "precip_2022":api_dict["year_2022"]["daily"]["precipitation_sum"],
            "precip_2021":api_dict["year_2021"]["daily"]["precipitation_sum"],
            "precip_2020":api_dict["year_2020"]["daily"]["precipitation_sum"],
            "precip_2019":api_dict["year_2019"]["daily"]["precipitation_sum"],
        }
        return precip_dict


# This method takes the precipitation dictionary, extracts just the values, converts them to floats, then sums the values.
    def precip_sum(self):
        precip_dict = self.precip_data('temp_2023', 'temp_2022', 'temp_2021', 'temp_2020', 'temp_2019')
        precip_values = [float(value[0]) for value in precip_dict.values()]
        total_precip = sum(precip_values)
        return total_precip
