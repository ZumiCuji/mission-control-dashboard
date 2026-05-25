import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

def get_neo_data():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={API_KEY}"
    r = requests.get(url)
    data = r.json()
    asteroids = []
    for date, objects in data["near_earth_objects"].items():
        for obj in objects:
            asteroids.append({
                "name": obj["name"],
                "date": date,
                "diameter_km": round(obj["estimated_diameter"]["kilometers"]["estimated_diameter_max"], 2),
                "velocity_kmh": round(float(obj["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]), 2),
                "miss_distance_km": round(float(obj["close_approach_data"][0]["miss_distance"]["kilometers"]), 2),
                "hazardous": obj["is_potentially_hazardous_asteroid"]
            })
    return sorted(asteroids, key=lambda x: x["miss_distance_km"])

def get_mars_weather():
    url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"
    r = requests.get(url)
    data = r.json()
    results = []
    for sol in data.get("sol_keys", []):
        sol_data = data[sol]
        results.append({
            "sol": sol,
            "avg_temp": sol_data.get("AT", {}).get("av", "N/A"),
            "min_temp": sol_data.get("AT", {}).get("mn", "N/A"),
            "max_temp": sol_data.get("AT", {}).get("mx", "N/A"),
            "pressure": sol_data.get("PRE", {}).get("av", "N/A"),
            "wind_speed": sol_data.get("HWS", {}).get("av", "N/A"),
        })
    return results

def get_satellite_data():
    # Uses public TLE data from CelesTrak (no key needed)
    url = "https://celestrak.org/SOCRATES/query.php?CODE=ISS&CAT=stations&FORMAT=json"
    r = requests.get("https://celestrak.org/pub/TLE/catalog.txt")
    lines = r.text.strip().split("\n")
    satellites = []
    for i in range(0, min(60, len(lines) - 2), 3):
        satellites.append({
            "name": lines[i].strip(),
            "line1": lines[i+1].strip(),
            "line2": lines[i+2].strip(),
        })
    return satellites[:20]
