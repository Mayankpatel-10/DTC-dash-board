// Initialize map
var map = L.map('map').setView([28.6139, 77.2090], 11);

L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 18
}).addTo(map);

// Simulated data for stats
function updateStats() {
    document.getElementById('activeBuses').textContent = Math.floor(Math.random() * 50) + 100;
    document.getElementById('alerts').textContent = Math.floor(Math.random() * 5) + " delays, " + Math.floor(Math.random() * 3) + " breakdowns";
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

// Modal implementation for alerting
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
    modal.innerHTML = `<h3>${section}</h3><p>Details will be available soon.</p>`;

    // Append modal and overlay to the body
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
}