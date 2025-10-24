# 🌦️ Weather Forecast CLI App (Python)

A simple yet powerful **Command-Line Interface (CLI)** weather application built in **Python**.  
It fetches **real-time weather data** using a **free API** (OpenWeatherMap) and displays temperature, humidity, wind speed, and weather conditions in a clean, readable format.

---

## 🚀 Features

- Get **current weather** for any city instantly.  
- Uses **OpenWeatherMap API** for real-time data.  
- Displays **temperature, humidity, pressure, and wind speed**.  
- Includes **error handling** for invalid city names or API issues.  
- Stores your **API key in a local JSON file** for easy configuration.  
- Built with **Object-Oriented Programming (OOP)** structure.  

---

## 🧠 Tech Stack

- **Language:** Python  
- **Libraries:** `requests`, `json`, `datetime`  
- **API:** [OpenWeatherMap](https://openweathermap.org/api)  

---

## 🖥️ How to Use

1. **Clone this repository**   
   git clone https://github.com/yourusername/weather-cli-app.git
   cd weather-cli-app

2. Install dependencies

pip install requests



3. Add your API key in config.json
    {
  "api_key": "your_openweathermap_api_key"
}

4. Run the app
   python weather_cli.py

5. Example Output
   Enter city name: London
-----------------------------
🌤  Weather in londan
Temperature: 18°C
Humidity: 65%
Wind Speed: 5.3 m/s
Condition: Clear sky
-----------------------------

