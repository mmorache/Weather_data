import requests

# Handle the API call requests
class APICalls:
    BASE_URL = "https://archive-api.open-meteo.com/v1/archive"
    PARAMS = {
        "latitude": 44.08,
        "longitude": -115.62,
        "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }

    def __init__(self, years):
        self.data = {}
        for year in years:
            self.data[f"year_{year}"] = self._fetch_data(year)

    def _fetch_data(self, year):
        params = {**self.PARAMS, "start_date": f"{year}-09-11", "end_date": f"{year}-09-11"}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_year_data(self):
        return self.data

# Get weather statistics
class WeatherStats:
    def __init__(self, api_data):
        self.api_data = api_data
        self.mean_temp = None
        self.max_wind = None
        self.sum_precip = None

    def _extract_weather_data(self, field):
        return {year: self.api_data[year]["daily"][field] for year in self.api_data}

    def _calculate_values(self, values, calculation):
        values = [float(value[0]) for value in values.values()]
        if calculation == "mean":
            self.mean_temp = sum(values) / len(values)
        
        elif calculation == "max":
            self.max_wind = max(values)

        elif calculation == "sum":
            self.sum_precip = sum(values)

    def _get_mean_temp(self):
        temp_data = self._extract_weather_data("temperature_2m_mean")
        return self._calculate_values(temp_data, "mean")

    def _get_max_wind(self):
        wind_data = self._extract_weather_data("wind_speed_10m_max")
        return self._calculate_values(wind_data, "max")

    def _get_sum_precip(self):
        precip_data = self._extract_weather_data("precipitation_sum")
        return self._calculate_values(precip_data, "sum")
    
    def get_stats(self):
        self._get_mean_temp()
        self._get_max_wind()
        self._get_sum_precip()