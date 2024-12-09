from flask_restful import Resource
from flask import request
import uuid

# Global in-memory data store
DATA_STORE = {
    "users": {}
}

class Home(Resource):
    def get(self):
        return {"message": "Welcome to Strava Lite API"}, 200

class RegisterUser(Resource):
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or 'age' not in data:
            return {"error": "Missing 'name' or 'age' field"}, 400

        user_id = str(uuid.uuid4())
        DATA_STORE['users'][user_id] = {
            "id": user_id,
            "name": data['name'],
            "age": data['age'],
            "workouts": [],
            "following": set()  # Stored as a set internally
        }
        # Create a copy of the user data and convert 'following' to a list
        user_copy = DATA_STORE['users'][user_id].copy()
        user_copy['following'] = list(user_copy['following'])
        return user_copy, 200

class UserResource(Resource):
    def get(self, user_id):
        user = DATA_STORE['users'].get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        # Return user data without 'workouts' and 'following'
        return {
            "id": user["id"],
            "name": user["name"],
            "age": user["age"]
        }, 200

    def delete(self, user_id):
        if user_id not in DATA_STORE['users']:
            return {"error": "User not found"}, 404
        del DATA_STORE['users'][user_id]
        return {}, 200

class ListUsers(Resource):
    def get(self):
        users_list = [
            {"id": user["id"], "name": user["name"], "age": user["age"]}
            for user in DATA_STORE['users'].values()
        ]
        return {"users": users_list}, 200

class AddWorkout(Resource):
    def put(self, user_id):
        user = DATA_STORE['users'].get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        data = request.get_json()
        if not data or 'date' not in data or 'time' not in data or 'distance' not in data:
            return {"error": "Missing 'date', 'time', or 'distance' field"}, 400

        workout = {
            "date": data['date'],
            "time": data['time'],
            "distance": data['distance']
        }
        user['workouts'].append(workout)
        return workout, 200

class ListWorkouts(Resource):
    def get(self, user_id):
        user = DATA_STORE['users'].get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {"workouts": user['workouts']}, 200

# Extra Credit
class FollowFriend(Resource):
    def put(self, user_id):
        user = DATA_STORE['users'].get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        data = request.get_json()
        if not data or 'follow_id' not in data:
            return {"error": "Missing 'follow_id' field"}, 400

        follow_id = data['follow_id']
        if follow_id not in DATA_STORE['users']:
            return {"error": "User to follow not found"}, 404

        user['following'].add(follow_id)
        following_list = list(user['following'])  # Convert set to list for JSON serialization
        return {"following": following_list}, 200

class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        user = DATA_STORE['users'].get(user_id)
        friend = DATA_STORE['users'].get(follow_id)
        if not user or not friend:
            return {"error": "User or friend not found"}, 404

        if follow_id not in user['following']:
            return {"error": "You are not following this user"}, 403

        return {"workouts": friend['workouts']}, 200
