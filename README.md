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

      curl -X POST http://localhost:5000/api/v1/users/ \
      -H "Content-Type: application/json" \
      -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}'

    * Retrieval:

      curl -X GET http://localhost:5000/api/v1/users/ (for all users)
      curl -X GET http://localhost:5000/api/v1/users/<user_id> (for specific user based on id)

    * Update:
      
      curl -X PUT http://localhost:5000/api/v1/users/<user_id> \
      -H "Content-Type: application/json" \
      -d '{"first_name": "John", "last_name": "Cena", "email": "john.cena@example.com"}'

    
  - Amenity:
 
    * Creation:

       curl -X POST http://localhost:5000/api/v1/amenities/ \
       -H "Content-Type: application/json" \
       -d '{"name": "Sink"}'

    * Retrieval:
   
      curl -X GET http://localhost:5000/api/v1/amenities/ (for all amenities)
      curl -X GET http://localhost:5000/api/v1/amenities/<amenity_id> (for specific amenity based on id)

    * Update:

      curl -X GET http://localhost:5000/api/v1/amenities/<amenity_id> \
      -H "Content-Type: application/json" \
      -d '{"name": "Cubards"}'
      
