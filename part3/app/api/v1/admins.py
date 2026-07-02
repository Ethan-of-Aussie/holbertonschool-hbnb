#!/usr/bin/python3
from app.services import facade
from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('admin', description='Admin operations')

@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @jwt_required()
    def put(self, user_id):

        user = facade.get_user(user_id)
        if not user:
            return {"error": "user not found"}, 404

        current_user = get_jwt()

        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        if not data:
            return {"error": "No data provided"}, 400

        email = data.get('email')
        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        protected = ['id', 'created_at', 'updated_at', 'is_admin']
        for field in protected:
            if field in data:
                return {"error": f"field {field} cannot be updated"}, 400

        if 'password'in data:
            data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # Logic to update user details, including email and password

        updated_user = facade.update_users(user_id, data)
        return {
            "id": updated_user.id,
            "first_name": updated_user.first_name,
            "last_name": updated_user.last_name,
            "email": updated_user.email,
            "status": "User updated successfully"
        }, 200

@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        if not user_data:
            return {"error": "No data provided"}, 400

        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
        except ValueError as e:
            return {"error": str(e)}, 400
        return {
            "id": new_user.id,
            "message": "User created successfully"
        }, 201


@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json
        if not amenity_data:
            return {"error": "No data provided"}, 400

        # Logic to create a new amenity
        try:
            new_amenity = facade.create_amenity(amenity_data)
        except ValueError as e:
            return {"error": str(e)}, 400
        return {
            "id": new_amenity.id,
            "name": new_amenity.name,
            "message": "Amenity created successfully"
        }, 201

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity = facade.get_amenity(amenity_id)
        if amenity is None:
            return {"error": "Amenity not found"}, 404

        amenity_data = request.json
        if not amenity_data:
            return {"error": "No data provided"}, 400

        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        except ValueError as e:
            return {"error": str(e)}, 400
        return {
            "id": updated_amenity.id,
            "name": updated_amenity.name,
            "message": "Amenity updated successfully"
        }, 200

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt()
        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = get_jwt_identity()

        place_data = request.json
        if not place_data:
            return {"error": "place not founded"}, 404
        if place_data["title"] == "":
            return {"error": "empty title"}, 400

        place = facade.get_place(place_id)
        if place is None:
            return {"error": "place not founded"}, 404

        if not is_admin:
            return {'error': 'Unauthorized action'}, 403

        updated_place = facade.update_place(place_id, place_data)

        return {
            "id": updated_place.id,
            "title": updated_place.title,
            "description": updated_place.description,
            "price": updated_place.price,
            "latitude": updated_place.latitude,
            "longitude": updated_place.longitude,
            "owner_id": updated_place.owner_id,
            "amenities": updated_place.amenities,
            "reviews": updated_place.reviews,
            "message": "Place updated successfully"
        }, 200
