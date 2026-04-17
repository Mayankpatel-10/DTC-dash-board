from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# API to get bus tracking data
@app.route('/api/bus-tracking')
def bus_tracking():
    # Simulated data for bus locations (latitude, longitude)
    buses = [
        {"id": 1, "lat": 28.6129, "lng": 77.2295},
        {"id": 2, "lat": 28.6331, "lng": 77.2200},
        {"id": 3, "lat": 28.6500, "lng": 77.2300},
        {"id": 4, "lat": 28.6139, "lng": 77.2090},
        {"id": 5, "lat": 28.5672, "lng": 77.2100}
    ]
    return jsonify(buses)

# API to get active buses and alert stats
@app.route('/api/stats')
def stats():
    # Simulated data for stats
    active_buses = random.randint(100, 150)
    alerts = {
        "delays": random.randint(1, 5),
        "breakdowns": random.randint(0, 3)
    }
    return jsonify({"active_buses": active_buses, "alerts": alerts})

if __name__ == '__main__':
    app.run(debug=True)