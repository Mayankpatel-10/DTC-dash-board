from flask import Flask, jsonify, render_template
import random
import csv
import os

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for Routes page
@app.route('/routes')
def routes_page():
    return render_template('routes.html')

# Route for Schedules page
@app.route('/schedules')
def schedules_page():
    return render_template('schedules.html')

# Route for Live Tracking page
@app.route('/live-tracking')
def live_tracking_page():
    return render_template('live-tracking.html')

# Route for Reports page
@app.route('/reports')
def reports_page():
    return render_template('reports.html')

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

# API to get main bus stops/terminals
@app.route('/api/main-points')
def main_points():
    main_stops = [
        {
            "id": 1,
            "name": "Kashmere Gate ISBT",
            "lat": 28.6791,
            "lng": 77.2295,
            "type": "Terminal",
            "capacity": "5000+ buses",
            "facilities": ["Parking", "Food Court", "Waiting Area", "Information Desk", "Rest Rooms"],
            "routes": ["101", "102", "103", "104", "105"],
            "description": "Major inter-state bus terminal with connectivity to Punjab, Haryana, UP"
        },
        {
            "id": 2,
            "name": "Connaught Place",
            "lat": 28.6308,
            "lng": 77.2177,
            "type": "Central Hub",
            "capacity": "2000+ buses",
            "facilities": ["Metro Connection", "Parking", "Shopping Complex", "Rest Rooms"],
            "routes": ["101", "102", "106", "107", "108"],
            "description": "Central business district with metro connectivity and major shopping areas"
        },
        {
            "id": 3,
            "name": "AIIMS Hospital",
            "lat": 28.5672,
            "lng": 77.2088,
            "type": "Medical Hub",
            "capacity": "1500+ buses",
            "facilities": ["Emergency Services", "Parking", "Waiting Area", "Medical Facilities"],
            "routes": ["103", "104", "109", "110", "111"],
            "description": "Premier medical institute with 24/7 emergency services and multiple bus connections"
        },
        {
            "id": 4,
            "name": "Dwarka Sector 21",
            "lat": 28.5711,
            "lng": 77.0844,
            "type": "Residential Hub",
            "capacity": "1800+ buses",
            "facilities": ["Metro Station", "Parking", "Market Area", "Bus Depot"],
            "routes": ["112", "113", "114", "115", "116"],
            "description": "Major residential and commercial hub with metro connectivity and large bus depot"
        },
        {
            "id": 5,
            "name": "Noida City Center",
            "lat": 28.5713,
            "lng": 77.3229,
            "type": "Corporate Hub",
            "capacity": "2200+ buses",
            "facilities": ["Metro Station", "Parking", "Corporate Offices", "Food Court"],
            "routes": ["117", "118", "119", "120", "121"],
            "description": "Major corporate and commercial center with extensive bus network and metro connectivity"
        },
        {
            "id": 6,
            "name": "Saket Select City Walk",
            "lat": 28.5280,
            "lng": 77.2069,
            "type": "Commercial Hub",
            "capacity": "1200+ buses",
            "facilities": ["Shopping Mall", "Metro Station", "Parking", "Entertainment"],
            "routes": ["122", "123", "124", "125", "126"],
            "description": "Premium shopping and entertainment destination with metro connectivity"
        },
        {
            "id": 7,
            "name": "Rohini Sector 18",
            "lat": 28.7355,
            "lng": 77.1186,
            "type": "Residential Hub",
            "capacity": "1600+ buses",
            "facilities": ["Metro Station", "Parking", "Market Area", "Educational Institutes"],
            "routes": ["127", "128", "129", "130", "131"],
            "description": "Large residential area with educational institutions and metro connectivity"
        },
        {
            "id": 8,
            "name": "Lajpat Nagar Central",
            "lat": 28.6479,
            "lng": 77.2450,
            "type": "Commercial Hub",
            "capacity": "1400+ buses",
            "facilities": ["Market", "Parking", "Metro Connection", "Business District"],
            "routes": ["132", "133", "134", "135", "136"],
            "description": "Traditional market area with modern commercial development and metro connectivity"
        },
        {
            "id": 9,
            "name": "Anand Vihar ISBT",
            "lat": 28.6475,
            "lng": 77.3161,
            "type": "Terminal",
            "capacity": "3000+ buses",
            "facilities": ["Parking", "Food Court", "Waiting Area", "Information Desk", "Rest Rooms"],
            "routes": ["137", "138", "139", "140", "141"],
            "description": "Eastern regional bus terminal with connectivity to UP and Bihar"
        },
        {
            "id": 10,
            "name": "Vasant Kunj Terminal",
            "lat": 28.5450,
            "lng": 77.1834,
            "type": "South Delhi Hub",
            "capacity": "1700+ buses",
            "facilities": ["Metro Station", "Parking", "Market Area", "Educational Hub"],
            "routes": ["142", "143", "144", "145", "146"],
            "description": "Major south Delhi transportation hub with educational institutions and metro connectivity"
        }
    ]
    return jsonify(main_stops)

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

# Function to read bus data from CSV
def read_bus_data():
    bus_data = []
    try:
        with open('bus_database.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bus_data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return bus_data

# API to get routes information
@app.route('/api/routes')
def routes():
    bus_data = read_bus_data()
    routes_list = []
    
    for i, bus in enumerate(bus_data[:20], 1):  # Show first 20 buses as routes
        stops_list = bus['Bus_Stops'].strip('"').split(', ')
        routes_list.append({
            "id": i,
            "name": f"Route {bus['Pickup_Point'].split()[0]}-{bus['Drop_Point'].split()[0]}",
            "bus_number": bus['Bus_Number'],
            "start": bus['First_Stop'],
            "end": bus['Last_Stop'],
            "distance": f"{len(stops_list) * 3} km",  # Approximate distance
            "stops": len(stops_list),
            "color": bus['Bus_Colour'],
            "status": bus['Status'],
            "first_run": bus['First_Run_Time'],
            "last_run": bus['Last_Run_Time']
        })
    
    return jsonify(routes_list)

# API to get schedules information
@app.route('/api/schedules')
def schedules():
    bus_data = read_bus_data()
    schedules_list = []
    
    for bus in bus_data[:15]:  # Show first 15 buses as schedules
        stops_list = bus['Bus_Stops'].strip('"').split(', ')
        route_name = f"{bus['Pickup_Point'].split()[0]}-{bus['Drop_Point'].split()[0]}"
        
        # Generate realistic arrival time based on stops
        departure_hour = int(bus['First_Run_Time'].split(':')[0])
        departure_min = int(bus['First_Run_Time'].split(':')[1])
        arrival_min = departure_min + len(stops_list) * 5  # 5 min per stop
        
        arrival_hour = departure_hour + (arrival_min // 60)
        arrival_min = arrival_min % 60
        
        # Random status
        import random
        status_options = ["On Time", "Delayed by 5 min", "Delayed by 10 min", "Early by 5 min"]
        status = random.choice(status_options)
        
        schedules_list.append({
            "route": route_name,
            "bus_number": bus['Bus_Number'],
            "departure": f"{departure_hour:02d}:{departure_min:02d} AM",
            "arrival": f"{arrival_hour:02d}:{arrival_min:02d} AM",
            "status": status,
            "color": bus['Bus_Colour'],
            "total_trips": bus['Total_Trips']
        })
    
    return jsonify(schedules_list)

# API to get reports information
@app.route('/api/reports')
def reports():
    bus_data = read_bus_data()
    
    # Calculate actual statistics from data
    total_buses = len(bus_data)
    active_buses = len([bus for bus in bus_data if bus['Status'] == 'Active'])
    inactive_buses = total_buses - active_buses
    
    # Generate realistic reports
    reports_data = {
        "daily_summary": {
            "total_buses": total_buses,
            "active_routes": len(set(f"{bus['Pickup_Point']}-{bus['Drop_Point']}" for bus in bus_data)),
            "total_passengers": random.randint(15000, 25000),
            "on_time_performance": f"{random.randint(85, 95)}%"
        },
        "weekly_summary": {
            "total_revenue": f"₹{random.randint(200000, 400000):,}",
            "average_delay": f"{random.randint(2, 8)}.{random.randint(0, 9)} minutes",
            "breakdowns": random.randint(5, 15),
            "complaints": random.randint(8, 20)
        },
        "alerts": [
            {"type": "warning", "message": f"Route {random.choice(bus_data)['Pickup_Point'].split()[0]} experiencing delays due to traffic"},
            {"type": "info", "message": f"New schedule implemented for Route {random.choice(bus_data)['Drop_Point'].split()[0]}"},
            {"type": "error", "message": f"Bus {random.choice(bus_data)['Bus_Number']} reported breakdown at {random.choice(bus_data)['Last_Stop']}"}
        ]
    }
    return jsonify(reports_data)

if __name__ == '__main__':
    app.run(debug=True)