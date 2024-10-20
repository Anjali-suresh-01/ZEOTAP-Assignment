import requests
import time
from datetime import datetime
from collections import defaultdict
import smtplib
import matplotlib.pyplot as plt

# Constants and settings
API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
TEMP_THRESHOLD = 35  # Temperature threshold in Celsius
ALERT_CONSECUTIVE_COUNT = 2  # Consecutive breaches for an alert

# Structures for storing data
weather_data = defaultdict(list)
daily_summary = defaultdict(dict)
alert_counts = defaultdict(int)  # Track consecutive breaches

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Fetch temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}")
        return None

# Function to process and store weather data
def process_weather_data(city, data):
    if data:
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_condition = data['weather'][0]['main']
        timestamp = data['dt']
        timestamp = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Store weather data
        weather_data[city].append({
            'temperature': temp,
            'feels_like': feels_like,
            'weather_condition': weather_condition,
            'timestamp': timestamp
        })
        
        # Update daily summary with new data
        update_daily_summary(city, temp, weather_condition)
        # Check if thresholds are breached
        check_thresholds(city, temp)

# Function to simulate continuous data fetching
def simulate_data_retrieval(interval=300):
    while True:
        for city in cities:
            data = fetch_weather_data(city)
            process_weather_data(city, data)
        time.sleep(interval)  # Wait for the interval before fetching again

# Function to update daily summary with weather data
def update_daily_summary(city, temp, weather_condition):
    today = datetime.now().strftime('%Y-%m-%d')
    
    if today not in daily_summary[city]:
        daily_summary[city][today] = {
            'temp_sum': 0,
            'temp_count': 0,
            'temp_max': float('-inf'),
            'temp_min': float('inf'),
            'weather_conditions': defaultdict(int)  # Track frequency of each condition
        }
    
    summary = daily_summary[city][today]
    
    # Update temperature stats
    summary['temp_sum'] += temp
    summary['temp_count'] += 1
    summary['temp_max'] = max(summary['temp_max'], temp)
    summary['temp_min'] = min(summary['temp_min'], temp)
    
    # Update weather condition frequency
    summary['weather_conditions'][weather_condition] += 1

# Function to calculate and return daily summaries
def calculate_daily_summary(city):
    today = datetime.now().strftime('%Y-%m-%d')
    if today in daily_summary[city]:
        summary = daily_summary[city][today]
        avg_temp = summary['temp_sum'] / summary['temp_count']
        max_temp = summary['temp_max']
        min_temp = summary['temp_min']
        dominant_weather = max(summary['weather_conditions'], key=summary['weather_conditions'].get)
        
        return {
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_weather': dominant_weather
        }
    else:
        return None

# Function to check thresholds and trigger alerts
def check_thresholds(city, temp):
    if temp > TEMP_THRESHOLD:
        alert_counts[city] += 1
    else:
        alert_counts[city] = 0  # Reset if below threshold
    
    if alert_counts[city] >= ALERT_CONSECUTIVE_COUNT:
        trigger_alert(city, temp)

# Function to trigger an alert
def trigger_alert(city, temp):
    print(f"ALERT: {city} temperature has exceeded {TEMP_THRESHOLD}°C for {ALERT_CONSECUTIVE_COUNT} consecutive updates.")
    send_email_alert(city, temp)

# Function to send an email alert
def send_email_alert(city, temp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    subject = f"Weather Alert for {city}"
    body = f"The temperature in {city} has exceeded {TEMP_THRESHOLD}°C. Current temperature: {temp}°C."
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", message)
    server.quit()

# Function to visualize weather trends for a city
def visualize_weather_data(city):
    dates = []
    avg_temps = []
    max_temps = []
    min_temps = []

    for date, summary in daily_summary[city].items():
        dates.append(date)
        avg_temps.append(summary['temp_sum'] / summary['temp_count'])
        max_temps.append(summary['temp_max'])
        min_temps.append(summary['temp_min'])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Avg Temperature')
    plt.plot(dates, max_temps, label='Max Temperature')
    plt.plot(dates, min_temps, label='Min Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f"Weather Summary for {city}")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("Starting Weather Monitoring System...")
    
    # Simulate real-time weather monitoring every 5 minutes (300 seconds)
    try:
        simulate_data_retrieval(interval=300)
    except KeyboardInterrupt:
        print("System stopped by user.")
    
    # Visualize weather data for a specific city
    visualize_weather_data("Delhi")
