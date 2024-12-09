from api import RegisterUser, UserResource, ListUsers, AddWorkout, ListWorkouts, FollowFriend, ShowFriendWorkouts

def init_routes(api):
    api.add_resource(RegisterUser, "/user")
    api.add_resource(UserResource, "/user/<string:user_id>")
    api.add_resource(ListUsers, "/users")
    api.add_resource(AddWorkout, "/workouts/<string:user_id>")
    api.add_resource(ListWorkouts, "/workouts/<string:user_id>")
    api.add_resource(FollowFriend, "/follow-list/<string:user_id>")
    api.add_resource(ShowFriendWorkouts, "/follow-list/<string:user_id>/<string:follow_id>")
