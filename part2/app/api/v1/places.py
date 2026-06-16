from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models.place import Place

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})
user_model = api.model(
    'User',
    {
        "id": fields.String,
        "first_name": fields.String,
        "last_name": fields.String,
        "email": fields.String
    }
)
amenity_model = api.model(
    'amenity_model',
    {
        "id": fields.String,
        "name": fields.String
    }
)
place_id_model = api.model(
    'place_id',
    {
        "id": fields.String,
        "title": fields.String,
        "description": fields.String,
        "latitude": fields.Float,
        "longitude": fields.Float,
        "owner": fields.Nested(user_model),
        "amenities": fields.List(fields.Nested(amenity_model))
    }
)


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        data = api.payload
        user = facade.get_user(data["owner_id"])
        if user == None:
            return {"message": "no user found"}, 400
        try:
            params_field = ["title", "description", "price", "latitude", "longitude"]
            place_params = {p_f:data[p_f] for p_f in params_field}
            place_params["owner"] = user
            created_place = facade.create_place(place_params).__dict__
        except Exception as e:
            return {"error": str(e)}, 400
        fields = ["id", "title", "description", "price", "latitude", "longitude"]
        print(created_place["owner"].__dict__["id"])
        place_dictionary = {field: created_place[field] for field in fields}
        place_dictionary["owner_id"] = created_place["owner"].__dict__["id"]
        return place_dictionary, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        data = facade.get_all_places()
        if not all(isinstance(p, Place) for p in data):
            raise TypeError("This is a place list")
        fields = ["id", "title", "latitude", "longitude"]
        res_dic = [{field: d.__dict__[field] for field in fields} for d in data]
        return res_dic, 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    @api.marshal_with(place_id_model)
    def get(self, place_id):
        """Get place details by ID"""
        data = facade.get_place(place_id)
        if data == None:
            return "Place dose not exist", 200
        return data, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        pass
