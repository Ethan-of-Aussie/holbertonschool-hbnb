from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from app.models.review import Review

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

review_output = api.model('Review', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer,
    'user_id': fields.String(attribute="user.id"),
    'place_id': fields.String(attribute="place.id")
    })

review_list_output = api.model('Review List Output', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer,  
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        place = facade.get_place(review_data.get("place_id"))
        user = facade.get_user(review_data.get("user_id"))
        fields = ["text", "rating"]
        review_params = {f:review_data[f] for f in fields}
        review_params["place"] = place
        review_params["user"] = user
        try:
            new_review = facade.create_review(review_params)
            return marshal(new_review, review_output), 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    @api.marshal_list_with(review_list_output)
    def get(self):
        """Retrieve a list of all reviews"""
        review_list = facade.get_all_reviews()
        return review_list, 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    @api.marshal_with(review_output)
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        return review, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload

        review = facade.update_review(review_id, review_data)

        return {'success': "Review update"}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        try:
            facade.delete_review(review_id)
            return {'success': 'Review successfully deleted'}, 200
        except ValueError as e:
            return {'error': str(e)}, 404
