// Make a GET request to the API server
fetch('http://127.0.0.1:1237/data')
    .then(response => {
        // Check if the response is successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON response
        return response.json();
    })
    .then(data => {
        // Display the data on the webpage
        // const dataContainer = document.getElementById('data-container');
        // dataContainer.innerHTML = JSON.stringify(data);

        console.log(data);

        const incidentCountElement = document.getElementById('incidentCount');
        incidentCountElement.textContent = data.length;

        const lastIncidentElement = document.getElementById('last-incident');
        lastIncidentElement.textContent = data[data.length - 1][1];

        const cameraElement = document.getElementById('cam-val');
        cameraElement.textContent = data[data.length - 1][3];
    })
    .catch(error => {
        // Handle any errors
        console.error('There was a problem with the fetch operation:', error);
    });



async function fetchItems() {
    try {
        const response = await fetch('http://localhost:1237/data');
        const data = await response.json();
        return data; // Assuming the response contains an array of incidents
    } catch (error) {
        console.error('Error fetching items:', error);
        return []; // Return an empty array in case of error
    }
}

// Function to render items
async function renderItems() {
    const itemList = document.getElementById('item-list');
    // Fetch items from the API
    const items = await fetchItems();
    // Clear previous items
    itemList.innerHTML = '';
    // Add items


    let lastLoc = document.querySelector(".last-location-view");
    lastLoc.addEventListener('click', function() {
        window.location.href = 'https://maps.google.com' + "/?q=" + items[items.length - 1][4] + ',' + items[items.length - 1][5]
    });


    items.forEach(incident => {
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('item1');

        const camera = document.createElement('h3');
        camera.classList.add('t-op-nextlvl');
        camera.textContent = incident[3];

        const time = document.createElement('h3');
        time.classList.add('t-op-nextlvl');
        time.textContent = incident[1];

        const date = document.createElement('h3');
        date.classList.add('t-op-nextlvl');
        date.textContent = incident[2];

        const location = document.createElement('h3');
        location.classList.add('t-op-nextlvl', 'label-tag');
        location.textContent = incident.slice(4, 6).join(', ');;

        location.addEventListener('click', function() {
            window.location.href = 'https://maps.google.com' + "/?q=" + incident[4] + ',' + incident[5];
        });

        itemDiv.appendChild(camera);
        itemDiv.appendChild(time);
        itemDiv.appendChild(date);
        itemDiv.appendChild(location);

        itemList.appendChild(itemDiv);
    });
}

// Initial rendering
renderItems();
