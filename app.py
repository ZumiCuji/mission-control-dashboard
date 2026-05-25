from flask import Flask, render_template, jsonify
from fetchers import get_neo_data, get_mars_weather, get_satellite_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/neo")
def neo():
    return jsonify(get_neo_data())

@app.route("/api/mars")
def mars():
    return jsonify(get_mars_weather())

@app.route("/api/satellites")
def satellites():
    return jsonify(get_satellite_data())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
