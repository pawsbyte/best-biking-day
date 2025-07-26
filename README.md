# 🚴 Best Biking Days Forecast

A simple Python app that helps you plan your bike rides by analyzing 7-day weather forecasts and suggesting the best days based on temperature, wind, and precipitation.

---

## 🌍 How It Works

1. **City Detection:**  
   Automatically detects your city using your IP address via the [ip-api.com](http://ip-api.com) service.

2. **Weather Forecast:**  
   Fetches a 7-day weather forecast from the [wttr.in](https://wttr.in) API in JSON format (no API key required).

3. **Ride Suitability Analysis:**  
   For each day, the app calculates a "biking suitability score" (0–100%) based on:
   - Temperature
   - Wind speed
   - Precipitation

4. **User-Friendly Output:**  
   Displays a clear, colorless table with the date, score, and reason for each rating.

---

## 📊 Example Output

-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Detecting your city based on IP address...
Your city: Amsterdam
Fetching 7-day weather forecast...

Best Days for Biking:
+------------+---------------+---------------------+
| Date       | Suitability   | Reason              |
+============+===============+=====================+
| 26.07.2025 | 100%          | Perfect conditions! |
+------------+---------------+---------------------+
| 27.07.2025 | 100%          | Perfect conditions! |
+------------+---------------+---------------------+
| 28.07.2025 | 100%          | Perfect conditions! |
+------------+---------------+---------------------+
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
