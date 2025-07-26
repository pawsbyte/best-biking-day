# Best Biking Days ☀️🚴‍♂️

A Python application that helps you find the best days for biking in your city based on weather conditions.

## 🌍 How It Works

1. **City Detection by IP:** Automatically detects your city using your IP address.
2. **Weather Forecast:** Fetches a 7-day weather forecast using [wttr.in](https://wttr.in).
3. **Biking Suitability Score:** Analyzes weather data to determine how suitable each day is for biking and provides reasons why.

## 📦 Requirements

- Python 3.8+
- `requests`
- `tabulate`

Install required packages with:

```bash
pip install requests tabulate
```

## 🚀 Usage

Simply run the script:

```bash
python app.py
```

Example output:

```
Detecting your city based on IP address...
Your city: Amsterdam
Fetching 7-day weather forecast...

Best Days for Biking:
+------------+---------------+------------------------------------+
| Date       | Suitability   | Reason                             |
+------------+---------------+------------------------------------+
| 26.07.2025 | 90%           | Warm weather (27°C); Light wind    |
| 27.07.2025 | 60%           | Rain: 2 mm; Moderate wind          |
| ...        | ...           | ...                                |
+------------+---------------+------------------------------------+
```

## 📈 How Scoring Works

- **Temperature:** Ideal range is 15°C–25°C. Too cold or too hot reduces the score.
- **Precipitation:** Rain decreases the score significantly.
- **Wind:** Strong winds reduce biking comfort.

## ❓ Why This Project

Biking is healthy, but weather can ruin your ride. This tool helps you plan ahead and pick the most comfortable and safe days for your trips.

© 2025 pawsbyte
