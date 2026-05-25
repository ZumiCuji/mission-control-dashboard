# Mission Control Dashboard 🚀

A real-time space data dashboard built with Python and Flask, pulling live data from NASA's public APIs.

## Features
- 🌍 **Near Earth Objects** — Live asteroid tracking with size, velocity, and miss distance
- 🔴 **Mars Weather** — Atmospheric readings from NASA's InSight lander
- 🛰️ **Orbital Object Tracker** — Live satellite tracking from CelesTrak

## Tech Stack
- Python, Flask, Plotly.js
- NASA NeoWs API, NASA InSight Weather API, CelesTrak TLE data
- Hosted on self-managed Ubuntu Linux server

## Setup
```bash
git clone https://github.com/ZumiCuji/mission-control-dashboard.git
cd mission-control-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```
