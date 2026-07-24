#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            // Your code to handle form submission
        });
    }
});

async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });
    // Handle the response
    if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = 'index.html';
} else {
    alert('Login failed: ' + response.statusText);
}
}

/*
index section of task-2
*/
async function logincheckAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        // Fetch places data if the user is authenticated
        const places = await fetchPlaces(token);
        displayPlaces(places);
    }
}
/*
Get cookie
 */
function getCookie(name) {
    // Function to get a cookie value by its name
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const parts = cookie.split('=');
        const key = parts[0];
        const value = parts[1];
        if (key === name) return value;
    }
    return null

}
// check if user auth'd by verifying jwt token in cookies
/*
Fetch places data:
Use the Fetch API to get the list of places and handle the response.
*/
async function fetchPlaces(token) {
    // Make a GET request to fetch places data
    const response = await fetch('http://localhost:5000/api/v1/places', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });
    // Include the token in the Authorization header
    if (!response.ok) {
        const err = await response.json()
        alert('Failed to fetch places:' + err.error);
        return null
    }
    return await response.json()
    // Handle the response and pass the data to displayPlaces function
}
/*
Populate places list:
Create HTML elements for each place and append them to the #places-list.
*/
function displayPlaces(places) {
    const place_list_id = document.querySelector('#places-list')
    place_list_id.innerHTML = '';
    // Clear the current content of the places list
    /* Could use insertAdjacentHTML. 
    The function in question can avoid the need to create div
    or use element.classlist.add and even the need to append */
    for (let data of places) {
        const newDiv = document.createElement("div");
        newDiv.classList.add("place-card")

        newDiv.innerHTML = `
           <h3>${data.name}</h3>
           <p>Price: $${data.price}</p>
           <p>${data.description}</p>      
        `// the double $ for data.price, one is variable insert and the other is a literal sign

        place_list_id.appendChild(newDiv)
    }
    // Iterate over the places data
    // For each place, create a div element and set its content
    // Append the created element to the places list
}
/*Implement client-side filtering:
Add an event listener to the price filter dropdown to filter places based on the selected price.
The filter will set the top price for the places to be shown.
The dropdown must be loaded with the following options:
10
50
100
All
*/

const pricefilter = document.querySelector("#price-filter");
const priceOptions = [10, 50, 100, "All"]
if (pricefilter) {
    priceOptions.forEach(value => {
        pricefilter.insertAdjacentHTML(
            "beforeend",
            `<option value="${value}">${value}</option>`
        )
    });
// Populating price-list ^    
}

document.getElementById('price-filter').addEventListener('change', async (event) => {
    const selectedPrice = event.target.value;
    // Get the selected price value
    const token = getCookie('token');
    const places = await fetchPlaces(token);
    const filtered = selectedPrice === "All" ? places :
    places.filter(p => p.price <= Number(selectedPrice));
    displayPlaces(filtered)
    // Iterate over the places and show/hide them based on the selected price
});

/*3.Place details Task */
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    // Extract the place ID from window.location.search
  
    return params.get("id")
}

function placecheckAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');
    const placeId = getPlaceIdFromURL();

    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
        // Store the token for later use
       
    } 
    fetchPlaceDetails(token, placeId).then(place => {
            if (place) displayPlaceDetails(place, token)
        });
}

async function fetchPlaceDetails(token, placeId) {
    const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
        method: 'GET',
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });
    // Make a GET request to fetch place details
    // Include the token in the Authorization header
    if (!response.ok) {
        const err = await response.json()
        alert('Failed to fetch places:' + err.error);
        return null
    }
    return await response.json()
    // Handle the response and pass the data to displayPlaceDetails function
}

function displayPlaceDetails(place, token) {
    const place_list_id = document.querySelector('#places-list')
    place_list_id.innerHTML = '';
    // Clear the current content of the place details section
    place_list_id.insertAdjacentHTML("beforeend",
        `
        <div class="place-details">
        <div class="place-info">
        <h3>${place.name}</h3>
        <p>${place.description}</p>
        <p>Price: $${place.price}</p>
        </div>

        <div class="place-amenities">
        <h3>Amenities</h3>
        <ul>
            ${place.amenities.map(a => `<li>${a.name}</li>`).join('')}
        </ul>
        </div>

        <div class="place-reviews">
        <h3>Reviews</h3>
            ${
                place.reviews.length > 0
                ?   place.reviews.map(r => 
                    `<div class="review-card">
                    <p>Comment: ${r.text}</p>
                    <p><strong>${r.user}</strong></p>
                    <p>Rating: ${r.rating}/5</p>
                    </div>`).join('')
                : `<p>No reviews yet</p>`}
       
        </div>
         ${token ? `
          <button onclick="window.location.href='add_review.html?id=${place.id}'">
          Add Review
          </button>  
        ` : ""}
          </div>
        `
    );
    // Create elements to display the place details (name, description, price, amenities and reviews)
    // Append the created elements to the place details section
}

/** Login and permission checks */
document.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector("#login-link")) {
        logincheckAuthentication();
    }
    if (document.querySelector("#add-review")) {
        placecheckAuthentication();
    }
});