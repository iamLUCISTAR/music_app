from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .user_manager import UserManager

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
user_api = Api(user_blueprint)


class User(Resource):
    """
    api to create new user and check if the user already exists
    """
    def post(self):
        try:
            request_dict = {'user_name': request.form['user_name'],
                            'email_id': request.form['email_id'],
                            'password': request.form['password']}
            resp = UserManager(request_dict).create_user()
            return resp
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp

user_api.add_resource(User, '/signup')


class UserLogin(Resource):
    def post(self):
        try:
            request_dict = {'email_id': request.form['email_id'],
                            'password': request.form['password']}
            resp = UserManager(request_dict).login_user()
            return resp
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


user_api.add_resource(UserLogin, '/login')


class UserLogout(Resource):
    def post(self):
        try:
            request_dict = {'email_id': request.form['email_id'],
                            'password': request.form['password']}
            resp = UserManager(request_dict).logout_user()
            return resp
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


user_api.add_resource(UserLogout, '/logout')
