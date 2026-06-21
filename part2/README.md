# Business logic and API implementation

## Requirements

- Python 3.x
- Flask
- Flask-RESTX

Operation of part 2

To get started and using the implementation, please follow the steps listed below:

- Cloning the repo
  
	```
  git clone https://github.com/Ethan-of-Aussie/holbertonschool-hbnb.git
 	```
  
- Navigating to target directory
  
    ```
	cd holbertonschool-hbnb/part2/
    ```

- Activating virtual environment
  
	```
    source venv/bin/activate
  	```

- Ignore previous step if using Holberton sandbox (ubuntu_2204)

- Installing required packages
  
    ```
    pip install -r requirements.txt
    ```

- Running the server
  
	```
    python3 run.py
  	```
  
Listed below are some example trial codes (curl) that can be used to check the functionality of the api calls.
  
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

	For owner_id, please use the generated user_id when creating user. Amenities can be left empty or the previously created amenity can be added. Please enclose them within "" when adding the amenitites.

	```
 	curl -X POST http://localhost:5000/api/v1/places/ \
      -H "Content-Type: application/json" \
      -d '{
		"title": "Cozy Apartment",
 		"description": "A nice place to stay",
  		"price": 100.0,
  		"latitude": 37.7749,
  		"longitude": -122.4194,
  		"owner_id": "",
  		"amenities": []
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

	For user_id and place_id please use the generated user_id and place_id when creating user and place.

	```
 	curl -X POST http://localhost:5000/api/v1/reviews/ \
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
      curl -X GET http://localhost:5000/api/v1/reviews/<review_id>
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
      curl -X DELETE http://localhost:5000/api/v1/reviews/<review_id>
	```

   Test files have also been created to test each of the end points which can be done by using:

   - python3 -m app.tests.testusers -v
   - python3 -m app.tests.testamenities -v
   - python3 -m app.tests.testplace -v
   - python3 -m app.tests.testreviews -v
