import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = '989c1a9dae696f70765c4a2500d6c6a4'  # Your real API key
CITY = 'Mangalore'

URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code != 200 or "list" not in data:
    print("Error fetching weather data.")
    exit()

# Extract forecast data
dates = [entry['dt_txt'] for entry in data['list'][:10]]
temps = [entry['main']['temp'] for entry in data['list'][:10]]

# Plotting
plt.figure(figsize=(12, 5))
sns.lineplot(x=dates, y=temps, marker='o')
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("weather_forecast_mangalore.png")
plt.show()
