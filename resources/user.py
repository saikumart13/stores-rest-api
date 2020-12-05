
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str, required=True, 
        help="This field cannot be blank")

    parser.add_argument('password',
        type=str, required=True,
        help="Password is required with username")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":f"User {data['username']} already exists, choose anothe name"}
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {"message":f"User {data['username']} created succesfully"}, 201
        

