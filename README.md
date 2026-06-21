# Holberton Bed&Breakfast
Getting started in making the Hbnb project!

## Contents
### Part 1

Documents:

- High Level Package Diagram

    Shows the relationship between our three layers (Presentation, Business Logic, Persistance)

- Class Diagram

    Shows the relationship between the four classes that we are planning to use which are:

    * User
    * Place
    * Review
    * Amenity

    The diagram also contains information about the attributes and methods of the individual classes.

- Sequence Diagram

  Shows the design of our API calls which are:
  
    * User Registration
    * Place Creation
    * Review Submission
    * Fetch List of Places

- Technical Document

  Shows the overall content of part 1 in one file. Contains all the diagrams with appropriate explaination.

### Part 2

  This part contains the implementation of the designs from Part 1 which has been divided into 5 sections.

  - api

    Contains the design and implementation of different end points for the 4 classes.

  - models

    Contains the object structure of each class.

  - persistence

    Contains the repository which has the methods that the methods in facade reference.

  - services

    Contains the facade which does the bulk of the operation called by the api.

  - tests

    Contains test files to test each of the end points of the 4 classes.

  Operation of part 2

  To get started and using the implementation, please follow the steps listed below:

  - source venv/bin/activate (to run in a virtual environment outside of Holberton sandbox)
  - pip install -r requirements.txt (to install the required packages)
  - python3 run.py (to run the server)
  
  - User:

    * Creation:
	```
      curl -X POST http://localhost:5000/api/v1/users/ \
      -H "Content-Type: application/json" \
      -d '{
		"first_name": "John", 
		"last_name": "Doe", 
		"email": "john.doe@example.com"
		}'
	```
    * Retrieval:
      For all users
	```
      curl -X GET http://localhost:5000/api/v1/users/
 	```
      For specific user based on id
	```
      curl -X GET http://localhost:5000/api/v1/users/<user_id>
	```

    * Update:
    ```
      curl -X PUT http://localhost:5000/api/v1/users/<user_id> \
      -H "Content-Type: application/json" \
      -d '{
    	"first_name": "John", 
		"last_name": "Cena", 
		"email": "john.cena@example.com"
		}'
	```
    
  - Amenity:
 
    * Creation:
	```
       curl -X POST http://localhost:5000/api/v1/amenities/ \
       -H "Content-Type: application/json" \
       -d '{"name": "Sink"}'
	```
    * Retrieval:
      For all amenities
	```
      curl -X GET http://localhost:5000/api/v1/amenities/
 	```
      For specific amenity based on id
	```
      curl -X GET http://localhost:5000/api/v1/amenities/<amenity_id>
	```
    * Update:
	```
      curl -X PUT http://localhost:5000/api/v1/amenities/<amenity_id> \
      -H "Content-Type: application/json" \
      -d '{"name": "Cubards"}'
 	```
  
  - Place:

    * Creation:

	For owner_id, please use the generated user_id when creating user.

	```
 	curl -X POST http://localhost:5000/api/v1/places/ \
      -H "Content-Type: application/json" \
      -d '{
		"title": "Cozy Apartment",
 		"description": "A nice place to stay",
  		"price": 100.0,
  		"latitude": 37.7749,
  		"longitude": -122.4194,
  		"owner_id": "" 
		}'
	```

    * Retrieval:
      For all places
	```
      curl -X GET http://localhost:5000/api/v1/places/
 	```
      For specific place based on id
	```
      curl -X GET http://localhost:5000/api/v1/places/<place_id>
	```

    * Update:
    ```
      curl -X PUT http://localhost:5000/api/v1/places/<place_id> \
      -H "Content-Type: application/json" \
      -d '{
  		"title": "Luxury Condo",
  		"description": "An upscale place to stay",
  		"price": 200.0
		}'
	```

  - Review:

	* Creation:

	For userr_id and place_id please use the generated user_id and place_id when creating user and place.

	```
 	curl -X POST http://localhost:5000/api/v1/places/ \
      -H "Content-Type: application/json" \
      -d '{
  		"text": "Great place to stay!",
  		"rating": 5,
  		"user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  		"place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
		}'
	```

    * Retrieval:
      For all reviews
	```
      curl -X GET http://localhost:5000/api/v1/reviews/
 	```
  
      For specific review based on id
	```
      curl -X GET http://localhost:5000/api/v1/reviewss/<review_id>
	```
  
      For all reviews for a specific place
	```
      curl -X GET http://localhost:5000/api/v1/places/<place_id>/reviews
	```

    * Update:
    ```
      curl -X PUT http://localhost:5000/api/v1/reviews/<review_id> \
      -H "Content-Type: application/json" \
      -d '{
  		"text": "Amazing stay!",
  		"rating": 4
		}'
	```

    * Delete:
    ```
      curl -X DELETE http://localhost:5000/api/v1/reviews/<review_id> \
	```
    
	
