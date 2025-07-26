import requests
from datetime import datetime
from tabulate import tabulate


def detect_city_by_ip():
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("status") == "success":
            return data.get("city")
    except Exception:
        pass
    return None


def fetch_weather_forecast(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def analyze_weather_day(day_data):
    temperature = float(day_data.get("avgtempC", 0))
    precipitation = float(day_data.get("precipMM", 0))
    wind_speed = float(day_data.get("avgwindKmph", 0)) / 3.6

    score = 100
    reasons = []

    if temperature < 5:
        score -= 40
        reasons.append(f"Too cold ({temperature}°C)")
    elif temperature > 30:
        score -= 40
        reasons.append(f"Too hot ({temperature}°C)")
    elif temperature < 15:
        score -= 10
        reasons.append(f"Cool weather ({temperature}°C)")
    elif temperature > 25:
        score -= 10
        reasons.append(f"Warm weather ({temperature}°C)")

    if precipitation > 0:
        score -= min(precipitation * 10, 50)
        reasons.append(f"Rain: {precipitation} mm")

    if wind_speed > 8:
        score -= 30
        reasons.append(f"Strong wind ({wind_speed:.1f} m/s)")
    elif wind_speed > 5:
        score -= 10
        reasons.append(f"Moderate wind ({wind_speed:.1f} m/s)")

    score = max(score, 0)
    if not reasons:
        reasons.append("Perfect conditions!")

    return score, "; ".join(reasons)


def format_forecast_results(forecast):
    days = forecast.get("weather", [])[:7]
    results = []

    for day in days:
        date_str = day.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d.%m.%Y")
        score, reason = analyze_weather_day(day)
        results.append([date, f"{score}%", reason])

    return results


def main():
    print("Detecting your city based on IP address...")
    city = detect_city_by_ip()

    if not city:
        city = input("Unable to detect. Please enter your city: ").strip()
        if not city:
            print("City is required.")
            return

    print(f"Your city: {city}")
    print("Fetching 7-day weather forecast...")

    forecast = fetch_weather_forecast(city)
    if not forecast:
        print("Failed to retrieve weather data.")
        return

    report = format_forecast_results(forecast)

    print("\nBest Days for Biking:")
    print(tabulate(report, headers=["Date", "Suitability", "Reason"], tablefmt="grid"))


if __name__ == "__main__":
    main()
