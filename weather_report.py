class WeatherReport:
    def __init__(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def display_weather(self):
        # Function to display the basic weather forecast for a city
        print(f"Weather in {self.city}: {self.temperature}°F, {self.condition}, Humidity: {self.humidity}%")