import requests
import json
from datetime import datetime

class WeatherApp:
    def __init__(self, api_key, history_file="weather_history.json"):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.history_file = history_file

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            self.display_weather(data)
            self.save_to_json(data)
        except requests.exceptions.RequestException as e:
            print(" Network Error:", e)
        except KeyError:
            print("⚠️ Unexpected data format received.")
        except Exception as e:
            print(" Error:", e)

    def display_weather(self, data):
        """Display formatted weather info"""
        print("\n🌤 Weather Report for:", data['name'])
        print("Temperature:", data['main']['temp'], "°C")
        print("Feels Like:", data['main']['feels_like'], "°C")
        print("Weather:", data['weather'][0]['description'].title())
        print("Humidity:", data['main']['humidity'], "%")
        print("Wind Speed:", data['wind']['speed'], "m/s")

    def save_to_json(self, data):
        """Save each city's weather data in JSON file"""
        record = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "weather": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed'],
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            history = []

        history.append(record)

        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=4)

        print(" Data saved to:", self.history_file)

    def show_history(self):
        """Show all saved weather records"""
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
                if not history:
                    print(" No history found yet.")
                    return
                print("\n===  Weather History ===")
                for record in history[-5:][::-1]:  # last 5 entries (latest first)
                    print(f"\n📅 {record['date_time']} - {record['city']}")
                    print(f"🌡 Temp: {record['temperature']} °C, Weather: {record['weather']}")
        except FileNotFoundError:
            print("📭 No history file found yet.")

    def run(self):
        """Main CLI Loop"""
        print("=== Weather CLI App (JSON Enabled) ===")
        while True:
            city = input("\nEnter city name (or 'history' / 'exit'): ").strip().lower()
            if city == 'exit':
                print("👋 Goodbye! Stay safe!")
                break
            elif city == 'history':
                self.show_history()
            elif city:
                self.get_weather(city)
            else:
                print("⚠️ Please enter a valid city name.")

if __name__ == "__main__":
    API_KEY = "add your api key here" #Note: The API key has been removed from this project due to GitHub privacy and security policies.  
    app = WeatherApp(API_KEY)
    app.run()

