#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            // Your code to handle form submission
            const email = document.querySelector('#email').value;
            const password = document.querySelector('#password').value;

            await loginUser(email, password)
        });
    }
});

async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/api/v1/auth/login/', {
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
    const response = await fetch('http://localhost:5000/api/v1/places/', {
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
    /* insertAdjacentHTML. 
    The function in question can avoid the need to create div
    or use element.classlist.add and even the need to append */
    for (let data of places) {
        place_list_id.insertAdjacentHTML("beforeend", `
        <div class="place-card">
           <h3>${data.title}</h3>
           <p>Price: $${data.price}</p>
           <p>${data.description}</p>
           <a href="place.html?id=${data.id}" class="details-button"><button>View Details</button></a>
           </div>      
        `)// the double $ for data.price, one is variable insert and the other is a literal sign
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
const priceOptions = [10, 50, 100, 150, 200, 250, "All"]
if (pricefilter) {
    priceOptions.forEach(value => {
        pricefilter.insertAdjacentHTML(
            "beforeend",
            `<option value="${value}">${value}</option>`
        )
    });
// Populating price-list ^    


    pricefilter.addEventListener('change', async (event) => {
        const selectedPrice = event.target.value;
        // Get the selected price value
        const token = getCookie('token');
        const places = await fetchPlaces(token);
        if (selectedPrice === "All") {
        displayPlaces(places); 
        } else {
        const filtered = places.filter(p => p.price <= Number(selectedPrice));
        displayPlaces(filtered);
        }
        // Iterate over the places and show/hide them based on the selected price
    });
}
/*3.Place details Task */
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    // Extract the place ID from window.location.search
  
    return params.get("id")
}


async function fetchPlaceDetails(token, placeId) {
    const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}/`, {
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
    const data = await response.json();
    displayPlaceDetails(data);
    // Handle the response and pass the data to displayPlaceDetails function
}

function displayPlaceDetails(place) {
    const place_list_id = document.querySelector('#place-details')
    place_list_id.innerHTML = '';
    // Clear the current content of the place details section
    place_list_id.insertAdjacentHTML("beforeend",
        `
        <div class="place-details">
        <div class="place-info">
        <h3>${place.title}</h3>
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
                    <p><strong>${r.first_name} ${r.last_name}</strong></p>
                    <p>Rating: ${r.rating}/5</p>
                    </div>`).join('')
                : `<p>No reviews yet</p>`
            }
       
        </div>
        <a href="add_review.html?id=${place.id}" class="add-review">
          <button>
          Add Review
          </button>
          </a>  
          </div>
        `
    );
    // Create elements to display the place details (name, description, price, amenities and reviews)
    // Append the created elements to the place details section
}

/* 
Add Review form task-4
*/

document.addEventListener('DOMContentLoaded', () => {
    const reviewForm = document.getElementById('review-form');
    
    const placeId = getPlaceIdFromURL();

    if (reviewForm) {
        const token = review_checkAuthentication();
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const reviewText = reviewForm.querySelector('#review').value;
            const reviewRating = reviewForm.querySelector('#rating').value;
            // Get review text from form
            const response = await submitReview(token, placeId, reviewText, reviewRating)
            // Make AJAX request to submit review
            /*handleResponse passes response body to check validation and to clear reviewForm */
            await handleResponse(response, reviewForm)
            // Handle the response
        });
    }
});
async function submitReview(token, placeId, reviewText, reviewRating) {
        return await fetch(`http://localhost:5000/api/v1/reviews/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`  
        },
        body: JSON.stringify({
            text: reviewText,
            rating: reviewRating,
            place_id: placeId
        })
        });

    // Make a POST request to submit review data
    // Include the token in the Authorization header
    // Send placeId and reviewText in the request body
    // Handle the response
}
async function handleResponse(response, reviewForm) {
    if (response.ok) {
        alert('Review submitted successfully!');
        reviewForm.reset();
        // Clear the form
    } else {
        const err = await response.json();
        alert('Failed to submit review:' + err.error);
    }
}
/** Login and permission checks */
function place_checkAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('review-form');
    const placeId = getPlaceIdFromURL();
    if (addReviewSection) {
    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
        // Store the token for later use 
    } 
    }
    fetchPlaceDetails(token, placeId)
}
async function login_checkAuthentication() {
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
function review_checkAuthentication() {
    const token = getCookie('token');
    if (!token) {
        window.location.href = 'index.html';
    }
    return token;
}
/* The checks are triggered when page detects an id */
document.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector("#login-form")) {
        login_checkAuthentication();
    }
    if (document.querySelector("#place-details")) {
        place_checkAuthentication();
    }
    if (document.querySelector("#review-form")) {
        review_checkAuthentication();
    }
});