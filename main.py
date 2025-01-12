from Weather_Finder import APICalls, WeatherStats

def main():
    # Get start and end years from user input
    start_year = int(input("Enter the start year: "))
    end_year = int(input("Enter the end year: "))

    # Generate the years list in reverse order
    years = list(range(end_year, start_year - 1, -1))

    # Create an instance of APICalls and fetch the data
    api_instance = APICalls(years)
    api_data = api_instance.get_year_data()

    # Create an instance of WeatherStats
    weather = WeatherStats(api_data)
    weather.get_stats()

    # Get the coordinates
    latitude = api_instance.PARAMS["latitude"]
    longitude = api_instance.PARAMS["longitude"]


    print(f"\n🌤️  Weather Statistics for {start_year} to {end_year} for {latitude}, {longitude}")
    print(f"\t🌡️  Mean Temperature: {weather.mean_temp:.2f}")
    print(f"\t🌬️  Max Wind Speed: {weather.max_wind:.2f}")
    print(f"\t☔ Total Precipitation: {weather.sum_precip:.2f}")

if __name__ == "__main__":
    main()
