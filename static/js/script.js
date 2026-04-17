// Initialize map
var map = L.map('map').setView([28.6139, 77.2090], 11);

L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
    attribution: ' OpenStreetMap contributors',
    maxZoom: 18
}).addTo(map);

// Simulated data for stats with smooth animations
function updateStats() {
    const activeBusesElement = document.getElementById('activeBuses');
    const alertsElement = document.getElementById('alerts');
    
    // Add fade effect for smooth updates
    activeBusesElement.style.opacity = '0.5';
    alertsElement.style.opacity = '0.5';
    
    setTimeout(() => {
        const newActiveBuses = Math.floor(Math.random() * 50) + 100;
        const newDelays = Math.floor(Math.random() * 5);
        const newBreakdowns = Math.floor(Math.random() * 3);
        
        activeBusesElement.textContent = newActiveBuses;
        alertsElement.textContent = newDelays + " delays, " + newBreakdowns + " breakdowns";
        
        // Fade back in
        activeBusesElement.style.opacity = '1';
        alertsElement.style.opacity = '1';
        
        // Add pulse animation
        activeBusesElement.classList.add('pulse');
        alertsElement.classList.add('pulse');
        
        setTimeout(() => {
            activeBusesElement.classList.remove('pulse');
            alertsElement.classList.remove('pulse');
        }, 1000);
    }, 300);
}

// Update stats every 5 seconds
updateStats();
setInterval(updateStats, 5000);

// Simulated bus locations
var buses = [
    [28.6129, 77.2295],
    [28.6331, 77.2200],
    [28.6500, 77.2300],
    [28.6139, 77.2090],
    [28.5672, 77.2100]
];

// Add bus markers to map
var busIcon = L.icon({
    iconUrl: 'bus-icon.png', // Add the correct path to your bus icon image
    iconSize: [30, 30]
});

buses.forEach(function(bus) {
    L.marker(bus, { icon: busIcon }).addTo(map);
});

// Modal implementation for showing actual data
function showAlert(section) {
    // Remove existing modals
    const existingOverlay = document.querySelector('.modal-overlay');
    const existingModal = document.querySelector('.modal');
    if (existingOverlay) existingOverlay.remove();
    if (existingModal) existingModal.remove();

    // Create overlay
    const overlay = document.createElement('div');
    overlay.classList.add('modal-overlay');
    overlay.addEventListener('click', function () {
        overlay.remove();
        modal.remove();
    });

    // Create modal
    const modal = document.createElement('div');
    modal.classList.add('modal');
    
    // Load data based on section
    loadSectionData(section, modal);

    // Append modal and overlay to the body
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
}

// Load data for different sections
async function loadSectionData(section, modal) {
    let content = `<h3>${section}</h3>`;
    
    try {
        let response;
        switch(section) {
            case 'Routes':
                response = await fetch('/api/routes');
                const routes = await response.json();
                content += '<div class="data-table"><table><tr><th>Route</th><th>Start Point</th><th>End Point</th><th>Distance</th><th>Stops</th></tr>';
                routes.forEach(route => {
                    content += `<tr><td>${route.name}</td><td>${route.start}</td><td>${route.end}</td><td>${route.distance}</td><td>${route.stops}</td></tr>`;
                });
                content += '</table></div>';
                break;
                
            case 'Schedules':
                response = await fetch('/api/schedules');
                const schedules = await response.json();
                content += '<div class="data-table"><table><tr><th>Route</th><th>Bus Number</th><th>Departure</th><th>Arrival</th><th>Status</th></tr>';
                schedules.forEach(schedule => {
                    const statusClass = schedule.status === 'On Time' ? 'status-on-time' : 'status-delayed';
                    content += `<tr><td>${schedule.route}</td><td>${schedule.bus_number}</td><td>${schedule.departure}</td><td>${schedule.arrival}</td><td class="${statusClass}">${schedule.status}</td></tr>`;
                });
                content += '</table></div>';
                break;
                
            case 'Live Tracking':
                response = await fetch('/api/bus-tracking');
                const buses = await response.json();
                content += '<div class="bus-tracking"><h4>Live Bus Locations</h4><div class="bus-list">';
                buses.forEach(bus => {
                    content += `<div class="bus-item">Bus ${bus.id}: Lat ${bus.lat}, Lng ${bus.lng}</div>`;
                });
                content += '</div></div>';
                break;
                
            case 'Reports':
                response = await fetch('/api/reports');
                const reports = await response.json();
                content += '<div class="reports-container">';
                content += '<div class="report-section"><h4>Daily Summary</h4>';
                content += `<p>Total Buses: ${reports.daily_summary.total_buses}</p>`;
                content += `<p>Active Routes: ${reports.daily_summary.active_routes}</p>`;
                content += `<p>Total Passengers: ${reports.daily_summary.total_passengers}</p>`;
                content += `<p>On-Time Performance: ${reports.daily_summary.on_time_performance}</p>`;
                content += '</div>';
                content += '<div class="report-section"><h4>Weekly Summary</h4>';
                content += `<p>Total Revenue: ${reports.weekly_summary.total_revenue}</p>`;
                content += `<p>Average Delay: ${reports.weekly_summary.average_delay}</p>`;
                content += `<p>Breakdowns: ${reports.weekly_summary.breakdowns}</p>`;
                content += `<p>Complaints: ${reports.weekly_summary.complaints}</p>`;
                content += '</div>';
                content += '<div class="report-section"><h4>Alerts</h4>';
                reports.alerts.forEach(alert => {
                    const alertClass = `alert-${alert.type}`;
                    content += `<div class="alert ${alertClass}">${alert.message}</div>`;
                });
                content += '</div>';
                content += '</div>';
                break;
                
            default:
                content += '<p>Details will be available soon.</p>';
        }
    } catch (error) {
        content += '<p>Error loading data. Please try again.</p>';
    }
    
    modal.innerHTML = content;
}