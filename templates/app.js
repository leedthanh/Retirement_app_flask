

// declare variable use houston as setview 
const htown_map = L.map('map-id').setView([29.749907, -95.358421], 9);

    // Add a base map layer (you can choose a different tile provider)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(htown_map);

    // Fetch the data and add GeoJSON to the map
    fetch('/5stars').then(response => response.json()).then(data => {
        L.geoJSON(data, {
            onEachFeature: function(feature, layer) {
                const popupContent = `
                    <b>Provider Name:</b> ${feature.properties["Provider Name"]}<br>
                    <b>Rating:</b> ${feature.properties["Overall Rating"]}<br>
                    <b>Location:</b> ${feature.properties["Location"]}
                `;
                layer.bindPopup(popupContent);
            }
        }).addTo(htown_map);});
