from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .user_manager import UserManager

user_blueprint = Blueprint('user', __name__)
user_api = Api(user_blueprint)


class User(Resource):
    """
    api to create new user and check if the user already exists
    """
    def post(self):
        request_dict = {'user_name': request.form['user_name'],
                        'email_id': request.form['email_id'],
                        'password': request.form['password']}
        msg = UserManager(request_dict).create_user()
        return msg

    """
    api to get user details of every user or by user_id"""
    def get(self):
        request_args = dict(request.args)
        request_data = {"user_id": request_args['user_id'] if request_args.get('user_id') else None}
        response = UserManager(request_data).get_user_details()
        return jsonify(response)


user_api.add_resource(User, '/user')


class UsersAuthentication(Resource):
    def get(self):
        return "Hello da mapla"


user_api.add_resource(UsersAuthentication, '/userlogin')
