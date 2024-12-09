from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from api import RegisterUser, UserResource, ListUsers, AddWorkout, ListWorkouts, FollowFriend, ShowFriendWorkouts

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(RegisterUser, "/user")
api.add_resource(UserResource, "/user/<string:user_id>")
api.add_resource(ListUsers, "/users") 
api.add_resource(AddWorkout, "/workouts/<string:user_id>")
api.add_resource(ListWorkouts, "/workouts/<string:user_id>") 
# Extra Credit:
api.add_resource(FollowFriend, "/follow-list/<string:user_id>")
api.add_resource(ShowFriendWorkouts, "/follow-list/<string:user_id>/<string:follow_id>")  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
