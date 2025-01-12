# Part C3  main.py file to call methods in C2
from Classes import weather_stats

# Creating instance of weather_stats
weather_data = weather_stats()

# Calling the weather variables in C2
print(f'Average Temperature {weather_data.mean_temp():.2f}')
print(f'Maximum Wind {weather_data.max_wind():.2f}')
print(f'Precipitation Total {weather_data.precip_sum():.2f}')
