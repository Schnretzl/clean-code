# 1. Refactoring a Weather Forecast Application into Classes and Modules

# Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.
from weather_report import WeatherReport

cities = {"New York": WeatherReport("New York", 70, "Sunny", 50),
          "London": WeatherReport("London", 60, "Cloudy", 65),
          "Tokyo": WeatherReport("Tokyo", 75, "Rainy", 70)}

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city == 'exit':
            break
        elif cities.get(city) == None:            
            print("City not found")
        else:
            cities[city].display_weather()

if __name__ == "__main__":
    main()











